import asyncio
import datetime
import logging
import random

from config import NIGHT_HOURS, ADMIN_CHAT_ID
from loader import *
from notifications import to_admin, to_users
from utils import utils
from commands.car_engine import model
import json

import sys
 
# setting path
sys.path.append('../../motormentor')

import scraper

logger = logging.getLogger()

def isNighttime(time: datetime.time) -> bool:
    return time.hour >= NIGHT_HOURS['start'] or time.hour < NIGHT_HOURS['end']

def getRandomNotifyTimeInTheMorning() -> datetime.time:
    return (datetime.datetime(2023,2,12 ,hour = NIGHT_HOURS['end'], minute=0, second=0) + datetime.timedelta(seconds=random.randint(60,600))).time()

class Timers:
    #Wrappers for loops
    #TODO dont like this function
    def run_everyday_at(time: datetime.time):
        def decorator(function):
            async def wrapper(*args, **kwargs):
                now = utils.now()
                next_run = now.replace(hour=time.hour, minute=time.minute, second=time.second)
                if next_run < now:
                    next_run+= datetime.timedelta(days=1)
                wait_time = (next_run - now).total_seconds()-1

                while True:
                    await asyncio.sleep(wait_time)
                    logging.info(f'Running task {function.__name__}')

                    await function(*args, **kwargs)
                    
                    now = utils.now()
                    next_run += datetime.timedelta(days=1)
                    wait_time = (next_run - now).total_seconds()
            return wrapper
        return decorator

    def run_every_round_hour():
        def decorator(function):
            async def wrapper(*args, **kwargs):
                now = utils.now()
                next_run = now.replace(hour=now.hour, minute=0, second=0)
                if next_run < now:
                    next_run += datetime.timedelta(hours=1)
                wait_time = (next_run - now).total_seconds()-1

                while True:
                    await asyncio.sleep(wait_time)
                    logging.info(f'Running task {function.__name__}')

                    await function(*args, **kwargs)
                    
                    now = utils.now()
                    next_run += datetime.timedelta(hours=1)
                    wait_time = (next_run - now).total_seconds()
            return wrapper
        return decorator

    def run_every(seconds):
        def decorator(function):
            async def wrapper(*args, **kwargs):
                while True:
                    logging.info(f'Running task {function.__name__}')
                    await function(*args, **kwargs)
                    
                    await asyncio.sleep(seconds)
            return wrapper
        return decorator

    def run_every_at_day(seconds):
        def decorator(function):
            async def wrapper(*args, **kwargs):
                while True:
                    if not isNighttime(datetime.datetime.now().time()):
                        logging.info(f'Running task {function.__name__}')
                        await function(*args, **kwargs)
                    
                    await asyncio.sleep(seconds)
            return wrapper
        return decorator

    #One time tasks
    async def run_in(seconds: int, func, *args, **kwargs):
        await asyncio.sleep(seconds)
        return await func(*args, **kwargs)
    
    async def run_at(time: datetime.time, func, *args, **kwargs):
        now = utils.now()
        next_run = now.replace(hour=time.hour, minute=time.minute, second=time.second,microsecond=time.microsecond)
        if next_run < now:
            next_run+= datetime.timedelta(days=1)
        wait_time = (next_run - now).total_seconds()
        await asyncio.sleep(wait_time)
        return await func(*args, **kwargs)

class Tasks:
    def __init__(self):
        asyncio.create_task(self.report_activity())
        asyncio.create_task(self.save_old_chats())
        asyncio.create_task(self.update_data())
        asyncio.create_task(self.check_user_subscriptions())
        asyncio.create_task(self.scrape_data())
    
    @Timers.run_every_at_day(3600)
    async def report_activity(self):
        await to_admin.report()

    @Timers.run_every_at_day(600)
    async def save_old_chats(self):
        cm.save_old_chats()


    df_columns = {
        'car_brand' : 'Toyota',
        'model' : 'camry',
        'year' : 2020,
        'engine_size' : 2.5,
        'engine_type' : 'gasoline',
        'mileage' : 50000,
        'body_type' : 'sedan',
        'transmission' : 'automatic',
        'drive_type' : 'front_wheel_drive',
        'condition' : 'car_is_not_damaged',
        'gas_equipment' : 'no',
        'steering_wheel' : 'left',
        'exterior_color' : 'white',
        'headlights' : 'led_headlights',
        'interior_color' : 'black',
        'interior_material' : 'leather',
        'sunroof' : 'no',
        'wheel_size' : 17
    }

    @Timers.run_everyday_at(datetime.time(hour=2, minute=30, second=0))
    async def scrape_data(self):
        logger.info("START TO SCRAPE")

        logger.info('Getting item ids...')

        itemids_len = len(scraper.ForSale.Cars.itemids)
        await scraper.ForSale.Cars.getItemIds()
        itemids_len = len(scraper.ForSale.Cars.itemids) - itemids_len

        logger.info(f'Found {itemids_len} listings')
        
        logger.info('Getting items...')
        if await scraper.ForSale.Cars.getItems():
            logger.info('Saving data...')
            scraper.ForSale.Cars.save()
        else:
            logger.info('Too many errors while scraping data, aborting...')
        scraper.ForSale.Cars.clear()

    @Timers.run_everyday_at(datetime.time(hour=11, minute=0, second=0))
    async def update_data(self):
        logger.info('Updating data...')
        new_cars_df = model.update()

        if new_cars_df is None or new_cars_df.empty:
            return
        
        df_columns = list(new_cars_df.columns)

        user_cars = db.fetchall('''SELECT sc.cid, sc.car_brand, sc.model,
        sc.year, sc.mileage_start, sc.mileage_end, sc.exterior_color, sc.body_type, sc.engine_type, sc.engine_size,sc.transmission,
        sc.drive_type,sc.condition, sc.gas_equipment,sc.steering_wheel, sc.price_start, sc.price_end, sc.id 
        FROM saved_cars AS sc
        JOIN users AS u ON sc.cid==u.cid WHERE sc.editing=0 AND u.subscription > 0;''')#TODO test this

        nMessages = 0
        for db_car in user_cars:
            db_car = {
                'cid':db_car[0],
                'car_brand':db_car[1],
                'model':db_car[2],
                'year':db_car[3],
                'mileage_start':db_car[4],
                'mileage_end':db_car[5],
                'exterior_color':db_car[6],
                'body_type':db_car[7],
                'engine_type':db_car[8],
                'engine_size':db_car[9],
                'transmission':db_car[10],
                'drive_type':db_car[11],
                'condition':db_car[12],
                'gas_equipment':db_car[13],
                'steering_wheel':db_car[14],
                'price_start':db_car[15],
                'price_end':db_car[16],
                'id':db_car[17]
            }
            
            query = ""
            for df_column in df_columns:
                if df_column in db_car.keys() and db_car[df_column]:
                    val = db_car[df_column]
                    if type(val) == int or type(val) == float or val.isnumeric():
                        query += f"`{df_column}` == {val} and "
                    else:
                        query += f"`{df_column}` == '{val}' and "

            if db_car['mileage_start']:
                query += f'mileage >= {db_car["mileage_start"]}'
            if db_car['mileage_end']:
                query += f' and mileage <= {db_car["mileage_end"]}'
            
            if db_car['price_start']:
                query += f' and dollar_price >= {db_car["price_start"]}'
            if db_car['price_end']:
                query += f' and dollar_price <= {db_car["price_end"]}'

            results = list(new_cars_df.query(query).index)
            
            nMessages += len(results)

            if len(results) > 0:
                #send notification
                await to_users.new_car(db_car['cid'], results)

                #save in db
                items = dict(json.loads(db.fetchone('SELECT found_cars FROM saved_cars WHERE id = ?', (db_car['id'],))[0]))
                items.update({datetime.datetime.now().date : itemid for itemid in results})
                db.query('UPDATE saved_cars SET found_cars = ? WHERE id = ?', (json.dumps(items), db_car['id']))


        logger.info(f'Data updated! Sent {nMessages} messages')


    @Timers.run_everyday_at(datetime.time(hour=12, minute=0, second=0))
    async def check_user_subscriptions(self):
        ended_users = db.query("SELECT cid FROM users WHERE subscription > 0 AND subscription_end < DATETIME('now')")
        db.query("UPDATE users SET subscription = 0 WHERE subscription > 0 AND subscription_end < DATETIME('now')")

        for cid in ended_users:
            await to_users.subscription_ended(cid)
import asyncio
import datetime
import logging
import random

from config import NIGHT_HOURS, ADMIN_CHAT_ID
from loader import *
from notifications import to_admin
from utils import utils

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
        #asyncio.create_task(self.check_masters_subscriptions())
    
    @Timers.run_every_at_day(3600)
    async def report_activity(self):
        await to_admin.report()



    @Timers.run_everyday_at(datetime.time(hour=1, minute=0, second=0))
    async def check_masters_subscriptions(self):
        pass
        # masters = db.fetchall("SELECT cid, trial_end_date, next_payment_date, account_state FROM masters WHERE account_state > ?;",(MASTER.ACCOUNT.NOT_ACTIVATED,))
        # now = utils.now()
        # now_time = now.time()
        # now_week_later = now + datetime.timedelta(days=config.DEACTIVATE_DAYS)
        
        # for mid, trial_end_date, next_payment_date, account_state in masters:
        #     if next_payment_date:
        #         subscription_end = utils.str2dt(next_payment_date)
        #     else:
        #         subscription_end = utils.str2dt(trial_end_date)

        #     if account_state == MASTER.ACCOUNT.ACTIVATED:
        #         if now_week_later > subscription_end:
        #             db.query('UPDATE masters SET account_state = ? WHERE cid = ?',(MASTER.ACCOUNT.CLOSE_PAYMENT, mid))
        #             if isNighttime(now_time):
        #                 notif_time = getRandomNotifyTimeInTheMorning()
        #                 asyncio.create_task(Timers.run_at(notif_time, to_master.subscription_end_close, mid))
        #                 continue
        #             await to_master.subscription_end_close(mid)
        #             await asyncio.sleep(0.1)

        #     if account_state == MASTER.ACCOUNT.CLOSE_PAYMENT:
        #         #if not paid dont take new appointments
        #         if now > subscription_end:
        #             db.query('UPDATE masters SET account_state = ? WHERE cid = ?',(MASTER.ACCOUNT.NOT_PAID, mid))
        #             if isNighttime(now_time):
        #                 notif_time = getRandomNotifyTimeInTheMorning()
        #                 asyncio.create_task(Timers.run_at(notif_time, to_master.subscription_end, mid))
        #                 continue
        #             await to_master.subscription_end(mid)
        #             await asyncio.sleep(0.1)

        #     if account_state == MASTER.ACCOUNT.NOT_PAID:
        #         #if not paid for a week deactivate account
        #         if now > subscription_end + datetime.timedelta(days=config.DEACTIVATE_DAYS):
        #             db.query('UPDATE masters SET account_state = ? WHERE cid = ?',(MASTER.ACCOUNT.DELETED, mid))
        #             if isNighttime(now_time):
        #                 notif_time = getRandomNotifyTimeInTheMorning()
        #                 asyncio.create_task(Timers.run_at(notif_time, to_master.account_deactivated, mid))
        #                 continue
        #             await to_master.account_deactivated(mid)
        #             await asyncio.sleep(0.1)
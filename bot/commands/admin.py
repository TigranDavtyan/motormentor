import asyncio
import inspect

import utils.utils as utils
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from buttons.buttons import *
from config import SUBSCRIPTION_DAYS
from phrases import phrases as P
from loader import *
from notifications import to_admin, to_users
from states.states import ADMIN, GENERAL,USER, State
import logging
import ad_engine
from .car_engine import model
from notifications import broadcast
import re
import json
import datetime

ad_channel = -1001901523079
logger = logging.getLogger()

@setActionFor(ADMIN.MENU)
async def admin_menu(message: Message, is_main_message: bool = False):
    cid, chat = message.chat.id, cm[message.chat.id]
    
    markup = Buttons()
    
    markup.add('Add advertisement', ADMIN.ADD_AD)
    markup.add('Show ads', ADMIN.SHOW_ADS)
    markup.add('Update data', ADMIN.UPDATE_DATA)
    markup.add('Broadcast message', ADMIN.BROADCAST)
    markup.add('Activate PREMIUM', ADMIN.ACTIVATE_PREMIUM)
   
    if not message.from_user.is_bot or is_main_message:
        await chat.send(P.menu(cid), markup, main_message=is_main_message)
    else:
        await chat.edit(P.menu(cid), markup)

    await chat.setState(ADMIN.MENU)


@setActionFor(ADMIN.ACTIVATE_PREMIUM)
async def activate_premium(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]
    await chat.edit('Formard any message from the user who you want to activate the PREMIUM subscription or type the user id')
    await chat.setState(ADMIN.ACTIVATE_PREMIUM)


@setActionFor(ADMIN.ACTIVATE_PREMIUM_HANDLE)
async def activate_premium_handle(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]
    if message.is_forward():
        user_id = message.forward_from.id
    else:
        user_id = int(message.text)
    
    user_data = db.fetchone('SELECT name, subscription, subscription_end FROM users WHERE cid=?', (user_id, ))
    if not user_data:
        await chat.send('No user found in database!', temporary=True)
        return
    
    name, sub, sub_end = user_data
    await chat.send(f'User id {user_id} | Name {name} | Sub {sub} | Date {sub_end}', temporary=True)

    if sub_end == '2025-01-01 00:00:00':
        new_sub_end = utils.now().replace(hour=0,minute=0,second=0,microsecond=0) + datetime.timedelta(days=SUBSCRIPTION_DAYS+1)
    else:
        new_sub_end = utils.str2dt(sub_end) + datetime.timedelta(days=SUBSCRIPTION_DAYS)

    db.query('UPDATE users SET subscription=1, subscription_end=? WHERE cid=?',(new_sub_end, cid))    

    await to_users.subscription_prolonged(user_id, new_sub_end)

    await chat.send(f'Subscription updated for the user. New subscription end date is {new_sub_end}', temporary=True)



@setActionFor(ADMIN.BROADCAST)
async def broadcast_message1(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]

    await chat.edit('Send a message to broadcast, you can include a link at the end like this "href=example.com"')
    await chat.setState(ADMIN.BROADCAST)

message_id = 0

async def edit_broadcast_message(message: Message, id):
    pattern = r"href=(.+)"
    match = re.search(pattern, message.caption[1:])

    if match:
        link = match.group(1)
        description = message.caption[0:match.span(1)[0]-4]

        link_button = Buttons()
        link_button.addLink(P.visit_website(0),  USER.LINK_CLICK, link)

        await bot.edit_message_caption(message.chat.id, id, caption=description, reply_markup=link_button.getMarkup())



@setActionFor(ADMIN.BROADCAST_HANDLE)
async def broadcast_message2(message: Message):
    global message_id
    cid, chat = message.chat.id, cm[message.chat.id]

    original_message = message

    new_id = (await bot.copy_message(cid, cid, message.message_id,)).message_id

    try:
        await edit_broadcast_message(message, new_id)
    except:
        await chat.send(P.wrong_action(cid), temporary=True)
        return
    
    message = await bot.forward_message(ad_channel, cid, new_id)
    message_id = message.message_id

    await chat.setState(ADMIN.BROADCAST_HANDLE)
    await chat.send('Are you sure? type "yes" or anything else.', temporary=True) 


@setActionFor(ADMIN.BROADCAST_CONFIRM)
async def broadcast_message3(message: Message):
    global message_id
    cid, chat = message.chat.id, cm[message.chat.id]

    if message.text.lower() == 'yes':
        await chat.send('Sending messages...')
        results = await broadcast.broadcast_users(ad_channel, message_id, False)
        nMessages = 0
        for res in results.values():
            nMessages += res
        result_text = f'''Broadcasted {nMessages} messages
Successfull      - {results[0]}
Blocked          - {results[1]}
Invalid user     - {results[2]}
Deactivated user - {results[3]}
TelegramAPIError - {results[4]}'''

        await chat.send(result_text)
    
        logger.info(result_text)
        message_id = ''
    else:
        await chat.send('Stopping the broadcast')
        await State.get(ADMIN.MENU)(message)


@setActionFor(ADMIN.UPDATE_DATA)
async def update_data(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]
    new_cars_df = model.update()

    # if new_cars_df is None or new_cars_df.empty:
    #     return
    
    # df_columns = list(new_cars_df.columns)

    # user_cars = db.fetchall('''SELECT cid, car_brand, model,
    # year, mileage_start, mileage_end, exterior_color, body_type, engine_type, engine_size,transmission,
    # drive_type,condition, gas_equipment,steering_wheel, price_start, price_end, id FROM saved_cars WHERE editing=0;''')

    # nMessages = 0
    # for db_car in user_cars:
    #     db_car = {
    #         'cid':db_car[0],
    #         'car_brand':db_car[1],
    #         'model':db_car[2],
    #         'year':db_car[3],
    #         'mileage_start':db_car[4],
    #         'mileage_end':db_car[5],
    #         'exterior_color':db_car[6],
    #         'body_type':db_car[7],
    #         'engine_type':db_car[8],
    #         'engine_size':db_car[9],
    #         'transmission':db_car[10],
    #         'drive_type':db_car[11],
    #         'condition':db_car[12],
    #         'gas_equipment':db_car[13],
    #         'steering_wheel':db_car[14],
    #         'price_start':db_car[15],
    #         'price_end':db_car[16],
    #         'id':db_car[17]
    #     }
        
    #     query = ""
    #     for df_column in df_columns:
    #         if df_column in db_car.keys() and db_car[df_column]:
    #             val = db_car[df_column]
    #             if type(val) == int or type(val) == float or val.isnumeric():
    #                 query += f"`{df_column}` == {val} and "
    #             else:
    #                 query += f"`{df_column}` == '{val}' and "

    #     if db_car['mileage_start']:
    #         query += f'mileage >= {db_car["mileage_start"]}'
    #     if db_car['mileage_end']:
    #         query += f' and mileage <= {db_car["mileage_end"]}'
        
    #     if db_car['price_start']:
    #         query += f' and dollar_price >= {db_car["price_start"]}'
    #     if db_car['price_end']:
    #         query += f' and dollar_price <= {db_car["price_end"]}'

    #     results = list(new_cars_df.query(query).index)
        
    #     nMessages += len(results)

    #     if len(results) > 0:
    #         #send notification
    #         await to_users.new_car(db_car['cid'], results)

    #         #save in db
    #         items = dict(json.loads(db.fetchone('SELECT found_cars FROM saved_cars WHERE id = ?', (db_car['id'],))[0]))
    #         items.update({str(datetime.datetime.now().date()) : itemid for itemid in results})
    #         db.query('UPDATE saved_cars SET found_cars = ? WHERE id = ?', (json.dumps(items), db_car['id']))


    # logger.info(f'Data updated! Sent {nMessages} messages')


'body_type == sedan and year == 2020 and engine_type == gasoline and engine_size == 2.5 and transmission == automatic and drive_type == front_wheel_drive and condition == car_is_not_damaged and gas_equipment == no and steering_wheel == left and exterior_color == white and mileage >= 45000.0 and mileage <= 55000.0 price >= 9500.0 and price <= 10500.0'

@setActionFor(ADMIN.SHOW_ADS)
async def add_ad(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]
    ads = db.fetchall('SELECT id, active, click_count, price, language, messageid FROM ads;')
    for ad in ads:
        id, active, click_count, price, language, messageid = ad
        keyboard = Buttons()
        keyboard.add('Delete', ADMIN.DELETE_AD, messageid)

        if int(active):
            keyboard.add('Disable', ADMIN.DISABLE_AD, messageid)
        else:
            keyboard.add('Activate', ADMIN.ACTIVATE_AD, messageid)

        await bot.copy_message(cid,ad_channel,messageid,reply_markup=keyboard.getMarkup())

@setActionFor(ADMIN.DELETE_AD)
async def delete_ad(message: Message, messageid):
    cid, chat = message.chat.id, cm[message.chat.id]
    print('Message ID = ',messageid)
    db.query('DELETE FROM ads WHERE messageid = ?', (messageid,))
    try:
        await bot.delete_message(ad_channel, messageid)
    except Exception as e:
        logging.info(e)

@setActionFor(ADMIN.DISABLE_AD)
async def disable_ad(message: Message, messageid):
    cid, chat = message.chat.id, cm[message.chat.id]

    db.query('UPDATE ads SET active = 0 WHERE messageid = ?', (messageid,))

@setActionFor(ADMIN.ACTIVATE_AD)
async def activate_ad(message: Message, messageid):
    cid, chat = message.chat.id, cm[message.chat.id]

    db.query('UPDATE ads SET active = 1 WHERE messageid = ?', (messageid,))

@setActionFor(ADMIN.ADD_AD)
async def add_ad(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]

    await chat.edit('''(PHOTO, VIDEO, MEDIA GROUP?)
0 (0-arm,1-ru, 2-eng)
Best super duper car gadget
for small medium big cars
Price-💳5000AMD(RUB,DOLLAR)
href=example.com''', Buttons(True))

    await chat.setState(ADMIN.ADD_AD)

@setActionFor(ADMIN.AD_HANDLE)
async def add_ad(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]
    original_message = message

    new_id = (await bot.copy_message(cid, cid, message.message_id,)).message_id

    lang, price = await ad_engine.edit_message(message, new_id)
    if lang is None:
        await chat.send(P.wrong_action(cid), temporary=True)
        return
    
    message = await bot.forward_message(ad_channel, cid, new_id)

    db.query('INSERT INTO ads (messageid, language, price) VALUES (?,?,?);', (message.message_id, lang, price))

    await State.get(ADMIN.MENU)(original_message)
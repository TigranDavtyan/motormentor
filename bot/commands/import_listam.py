import ast
import re
import sys

import utils.utils as utils
from aiogram.types import Message
from buttons.buttons import *
from config import LISTAM_ID_APPENDER
from loader import *
from phrases import phrases as P
from states.states import ADMIN, GENERAL, USER, State

from .car_engine import Car, XGBModel

sys.path.append('../../motormentor')

from data_storage import db as data_db
from scraper_listam import ListAm


@setActionFor(USER.IMPORT_LISTAM.INFO)
async def import_listam(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    listamurl = Buttons(True)
    listamurl.addLink('List.am', USER.IMPORT_LISTAM.INFO, 'https://www.list.am/en/category/23')#TODO

    await chat.edit(P.list_am_usage(cid), listamurl)
    await chat.setState(USER.IMPORT_LISTAM.INFO)


@setActionFor(USER.IMPORT_LISTAM.HANDLE_URL)
async def handle_listam_url(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]
    
    try:
        item_id = int(re.search(r"/(\d+)$", message.text).group(1))
    except:
        await chat.send(P.wrong_action(cid), temporary=True)

    properties = ListAm().getItemProperties(item_id)
    if not properties:
        await chat.send(P.listam_not_possible(cid), temporary=True)
        return
    
    car = Car(cid, properties = properties)

    markup = Buttons(True)
    markup.add(P.import_data(cid), USER.CAR_PRICE.INFO)
    markup.add(P.show_price_updates(cid), USER.IMPORT_LISTAM.SHOW_UPDATES, item_id)
    markup.add(P.follow_price_updates(cid), USER.IMPORT_LISTAM.FOLLOW_UPDATES, item_id)

    await chat.edit(f'<b>{car.getBrand()} {car.getModel()} {car.engine_size}L</b>\n\n'+P.listam_what_to_do(cid), markup)
    await chat.setState(USER.IMPORT_LISTAM.HANDLE_URL)


@setActionFor(USER.IMPORT_LISTAM.FOLLOW_UPDATES)
async def follow_price_updates(message: Message, data):
    cid, chat = message.chat.id,cm[message.chat.id]

    itemid = int(data)

    properties = ListAm().getItemProperties(itemid)
    car_brand, car_model, year, engine_size, price = properties['car_brand'], properties['model'], properties['year'], properties['engine_size'], properties['dollar_price']
    db.query('INSERT INTO follow_listing (url, cid, car_brand, model, year, engine_size, last_price) VALUES (?,?,?,?,?,?,?)',
             ('list.am/en/item/'+str(itemid), cid, car_brand, car_model, year, engine_size, price))
    await chat.send(P.follow_successfull(cid, car_brand, car_model, year, engine_size, price), temporary=True)


@setActionFor(USER.IMPORT_LISTAM.SHOW_UPDATES)
async def show_price_updates(message: Message, data):
    cid, chat = message.chat.id,cm[message.chat.id]
    itemid = int(data)
    
    updates = ast.literal_eval(data_db.fetchone('SELECT updates FROM listings WHERE itemid = ?',(itemid+LISTAM_ID_APPENDER,))[0])

    if len(updates) == 0:
        await chat.send(P.no_price_updates(cid), temporary=True)
        return

    text = ''
    for i, update in enumerate(updates.items()):
        if update[1] == -1:
            continue
        date_str = str(update[0])[:10]
        text += f'\n{i+1} | {date_str}   {round(update[1])}$'
    
    if text == '':
        await chat.send(P.no_price_updates(cid), temporary=True)
    else:
        await chat.send(text, temporary=True)

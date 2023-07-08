import sys

import logging

import config
from aiogram.types import Message
from loader import *
from phrases import phrases as P
from utils import logging as lgm
from utils import utils
from buttons.buttons import Buttons, setActionFor
from states.states import USER

logger = logging.getLogger()

listam_url = 'list.am/item/{itemid}'
myautoge_url = 'myauto.ge/en/pr/{itemid}'

async def new_car(cid, itemids: list):
    chat = cm[cid]
    item_links = ''
    for i, itemid in enumerate(itemids):
        if itemid < config.MYAUTOGE_ID_APPENDER:
            url = listam_url.format(itemid = itemid - config.LISTAM_ID_APPENDER)
        else:
            url = myautoge_url.format(itemid = itemid - config.MYAUTOGE_ID_APPENDER)

        item_links += f'{i+1} - {url}\n'

    await chat.send(P.found_saved_car(cid, len(itemids)) + item_links, temporary=True)

async def subscription_ended(cid):
    chat = cm[cid]
    await chat.send(P.subscription_end(cid), temporary=True)
    logger.info(f'User {cid} subscription ended.')

async def subscription_prolonged(user_id, new_sub_end):
    chat = cm[user_id]
    await chat.send(P.payment_successfull(user_id, new_sub_end.date()))
    logger.info(f'User {user_id} subscription prolonged to {new_sub_end}.')
    

async def car_price_update(cid, url, car_brand, model, year, engine_size, last_price, new_price):
    chat = cm[cid]
    remove_follow = Buttons()
    remove_follow.add(P.remove_follow(cid), USER.REMOVE_FOLLOW, url)
    await chat.send(P.notify_price_update(cid, car_brand, model, year, engine_size, last_price, new_price, url), remove_follow)


@setActionFor(USER.REMOVE_FOLLOW)
async def remove_follow(message: Message, data):
    cid, chat = message.chat.id, cm[message.chat.id]
    db.query('DELETE FROM follow_listing WHERE cid = ? AND url = ?;', (cid, data))
    await bot.delete_message(cid, message.message_id)
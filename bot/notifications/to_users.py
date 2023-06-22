import sys

import logging

import config
from aiogram.types import Message
from loader import *
from phrases import phrases as P
from utils import logging as lgm
from utils import utils

logger = logging.getLogger()

async def new_car(cid, itemids: list):
    chat = cm[cid]
    item_links = ''
    for i,itemid in enumerate(itemids):
        item_links += f'{i+1} - list.am/item/{itemid}'
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
    await chat.send(P.notify_price_update(cid, car_brand, model, year, engine_size, last_price, new_price, url))

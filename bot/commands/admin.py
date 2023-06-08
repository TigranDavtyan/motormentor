import asyncio
import inspect

import utils.utils as utils
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from buttons.buttons import *
from config import ADMIN_CHAT_ID, DEFAULT_LANGUAGE
from phrases import phrases as P
from loader import *
from notifications import to_admin
from states.states import ADMIN, GENERAL,USER, State
import logging
import ad_engine
from .car_engine import model

ad_channel = -1001901523079

@setActionFor(ADMIN.MENU)
async def admin_menu(message: Message, is_main_message: bool = False):
    cid, chat = message.chat.id, cm[message.chat.id]
    
    markup = Buttons()
    
    markup.add('Add advertisement', ADMIN.ADD_AD)
    markup.add('Show ads', ADMIN.SHOW_ADS)
    markup.add('Update data', ADMIN.UPDATE_DATA)
   
    if not message.from_user.is_bot or is_main_message:
        await chat.send(P.menu(cid), markup, main_message=is_main_message)
    else:
        await chat.edit(P.menu(cid), markup)

    await chat.setState(ADMIN.MENU)

@setActionFor(ADMIN.UPDATE_DATA)
async def update_data(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]
    model.update()
    await chat.send('Data updated!',temporary=True)

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
    # new_id = (await bot.forward_message(cid, cid, message.message_id)).message_id

    lang, price = await ad_engine.edit_message(message, new_id)
    if lang is None:
        await chat.send(P.wrong_action(cid), temporary=True)
        return
    
    message = await bot.forward_message(ad_channel, cid, new_id)

    db.query('INSERT INTO ads (messageid, language, price) VALUES (?,?,?);', (message.message_id, lang, price))

    await State.get(ADMIN.MENU)(original_message)
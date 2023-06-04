import random
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from buttons.buttons import *
from loader import *
from states.states import ADMIN, GENERAL,USER, State
import re
from phrases import phrases as P

ad_channel = -1001901523079
languages = {'arm': 0, 'ru' : 1, 'en' : 2}

async def sendAdTo(cid):
    chat = cm[cid]
    ads = db.fetchall('''SELECT id, messageid, price FROM ads WHERE active = 1''')#TODO check language
    if len(ads) == 0:
        return None
    
    ad = random.choice(ads)

    await bot.forward_message(cid,ad_channel,ad[1])
    return True


async def edit_message(message: Message, id):
    pattern = r"\s*href=(\S+)"

    match = re.search(pattern, message.caption[1:])
    if match:
        language = int(message.caption[0])
        description = message.caption[2:match.span(1)[0]-4]
        link = match.group(1)
    else:
        return None, None
    pattern = r"💳(\d+)([A-Z]+)"

    match = re.search(pattern, message.caption)
    price = -1
    currency = ''
    if match:
        price = match.group(1)
        currency = match.group(2)

    link_button = Buttons()
    link_button.addLink(P.visit_website(language),  USER.LINK_CLICK, link)

    await bot.edit_message_caption(message.chat.id, id, caption=description,reply_markup=link_button.getMarkup())
    return language, str(price)+currency



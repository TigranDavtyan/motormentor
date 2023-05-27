import sys
sys.path.append('../bot/')

from loader import *
from aiogram.types import Message
from phrases import phrases as P
import logging
from utils import utils
import config
from utils import logging as lgm

async def new_user(message: Message):
        text = f"""New user {message.from_user.full_name}
ID - {message.chat.id}
Username - {message.from_user.username}
Language - {message.from_user.language_code}"""
        
        photos = await message.from_user.get_profile_photos()
        
        if photos.total_count > 0:
            try:
                await cm[config.ADMIN_CHAT_ID].send(text,photo=photos.photos[0][0].file_id, temporary=True)
            except Exception as e:
                print(e)
                await cm[config.ADMIN_CHAT_ID].send(text, temporary=True)
        else:
            await cm[config.ADMIN_CHAT_ID].send(text, temporary=True)
        logging.info(f'NOTIF: ADMIN - {config.ADMIN_CHAT_ID} new user {message.chat.id}')

async def report_log(log_message):

    await cm[config.REPORT_CHANNEL_ID].send(log_message, disable_notification=True)

async def report():
    text = "Report for the last 1 hour\n"
    for userid, activity in lgm.user_activity.items():
        text += f"{db.getUserName(userid)}:{userid} sent - {activity['sent']}\n"

    await cm[config.REPORT_CHANNEL_ID].send(text, disable_notification=True)
    lgm.user_activity = {}
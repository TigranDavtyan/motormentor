import asyncio
import logging

from loader import *
from aiogram.utils import exceptions, executor
log = logging.getLogger('broadcast')

def get_users():
    return [u[0] for u in db.fetchall('SELECT cid FROM users;')]
def get_masters():
    return [u[0] for u in db.fetchall('SELECT cid FROM masters;')]


async def send_message(user_id: int, text: str, disable_notification: bool = False) -> int:
    """
    Safe messages sender

    :param user_id:
    :param text:
    :param disable_notification:
    :return:
    """
    try:
        await bot.send_message(user_id, text, disable_notification=disable_notification) 
    except exceptions.BotBlocked:
        log.error(f"Target [ID:{user_id}]: blocked by user")
        return 1
    except exceptions.ChatNotFound:
        log.error(f"Target [ID:{user_id}]: invalid user ID")
        return 2
    except exceptions.RetryAfter as e:
        log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_message(user_id, text)  # Recursive call
    except exceptions.UserDeactivated:
        log.error(f"Target [ID:{user_id}]: user is deactivated")
        return 3
    except exceptions.TelegramAPIError:
        log.exception(f"Target [ID:{user_id}]: failed")
        return 4
    else:
        log.info(f"Target [ID:{user_id}]: success")
        return 0

async def broadcast_users(message: str) -> int:
    """
    Simple broadcaster

    :return: Count of messages
    """
    results = {0:0, 1:0, 2:0, 3:0, 4:0}

    for user_id in set(get_users()):
        res = 4
        retry = 3
        while retry > 0 and res == 4:
            res = await send_message(user_id, message)
            await asyncio.sleep(.05)  # 20 messages per second (Limit: 30 messages per second)

        results[res] += 1

    return results

async def broadcast_masters(message: str) -> int:
    """
    Simple broadcaster

    :return: Count of messages
    """
    results = {0:0, 1:0, 2:0, 3:0, 4:0}

    for user_id in set(get_masters()):
        res = 4
        retry = 3
        while retry > 0 and res == 4:
            res = await send_message(user_id, message)
            await asyncio.sleep(.05)# 20 messages per second (Limit: 30 messages per second)

        results[res] += 1
          
    return results
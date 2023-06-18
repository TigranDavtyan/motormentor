from loader import *
from aiogram.types import Message
from phrases import phrases as P
from states.states import USER
from buttons.buttons import setActionFor, Buttons
from config import BOT_USERNAME, BONUS_REFS, BONUS_DAYS_FOR_REFS
import datetime
from utils import utils

@setActionFor(USER.SUBSCRIPTION.INFO)
async def subscription_info(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    sub_data = db.fetchone('SELECT subscription, subscription_end FROM users WHERE cid = ?;', (cid,))

    if sub_data[0] == 0:
        await chat.edit(P.sub_info_free(cid), Buttons(True))
    elif sub_data[0] == 1:
        sub_end = utils.str2dt(sub_data[1])
        days_left = (utils.now() - sub_end).days
        await chat.edit(P.sub_info_premium(cid, days_left), Buttons(True))

    await chat.setState(USER.SUBSCRIPTION.INFO)
    
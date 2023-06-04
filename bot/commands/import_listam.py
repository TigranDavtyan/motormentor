import utils.utils as utils
from aiogram.types import Message
from buttons.buttons import *
from loader import *
from phrases import phrases as P
from states.states import ADMIN, GENERAL, USER, State
from .car_engine import model, Car
import re

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

    df = model.getData()

    try:
        item = df.loc[item_id]
    except:
        await chat.send(P.listam_not_possible(cid), temporary=True)
        return
    
    Car(cid, item)
    await State.get(USER.CAR_PRICE.INFO)(message)

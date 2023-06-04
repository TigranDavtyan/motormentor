from loader import *
from aiogram.types import Message
from phrases import phrases as P
from states.states import USER, GENERAL
from buttons.buttons import *

@setActionFor(USER.MAIN_MENU)
async def cmd_menu_user(message: Message, is_main_message: bool = False):
    cid = message.chat.id
    chat = cm[cid]

    markup = Buttons()

    markup.add(P.get_car_price(cid), USER.CAR_PRICE.INFO)
    markup.add(P.import_from_listam(cid), USER.IMPORT_LISTAM.INFO)
    markup.add(P.general_info(cid), USER.INFO_PAGE)
    markup.add(P.language_change(cid), GENERAL.LANGUAGE.CHOOSE)

    if not message.from_user.is_bot or is_main_message:
        await chat.send(P.main_menu(cid), markup, main_message=is_main_message)
    else:
        await chat.edit(P.main_menu(cid), markup)

    await chat.setState(USER.MAIN_MENU)

@setActionFor(USER.INFO_PAGE)
async def info_page(message: Message):
    cid = message.chat.id
    chat = cm[cid]

    markup = Buttons(True)
    await chat.edit(P.start(cid), markup)
    await chat.setState(USER.INFO_PAGE)
import asyncio
import inspect

from utils import utils
from aiogram.types import CallbackQuery, Message
from buttons.buttons import *
from config import ADMIN_CHAT_ID, DEFAULT_LANGUAGE
from phrases import phrases as P
from loader import *
from notifications import to_admin
from states.states import ADMIN, GENERAL,USER, State
from utils.logging import logging
import ad_engine

languages = {'arm': 0, 'ru' : 1, 'en' : 2}

async def checkUserSubscription(chat, new_state: State):
    sub = db.fetchone('SELECT subscription FROM users WHERE cid = ?',(chat.cid,))[0]
    if sub >= new_state.min_subscription:
        return True
    
    await chat.send(P.subscription_not_enough(chat.cid, sub, new_state.min_subscription))
    return False

@dp.callback_query_handler(button_cb.filter(type='main'))
async def callback_query_handler(query: CallbackQuery, callback_data: dict):
    chat = cm[query.message.chat.id]

    if callback_data['action'] == 'back':
        await chat.back(query.message)
        return
    
    state_id = int(callback_data['action'])
    state = State.get(state_id)

    if not await checkUserSubscription(chat, state):
        return

    argspec = inspect.getfullargspec(state.ACTION)

    if callback_data['data'] == '-':
        if 'query_id' in argspec.args:
            await state(query.message, query.id)
        else:
            await state(query.message)
    else:
        if 'query_id' in argspec.args:
            await state(query.message, callback_data['data'], query.id)
        else:
            await state(query.message, callback_data['data'])


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def message_handler_handler(message: Message):
    chat = cm[message.chat.id]
    if message.text :
        if message.text.startswith('/start'):
            return await State.get(GENERAL.START)(message)
        if message.text.startswith('/help'):
            return await chat.send(P.help(chat.cid), temporary=True)
        
    state_id = chat.getState()
    state = State.get(State.get(state_id).NEXT)

    if not await checkUserSubscription(chat, state):
        return

    await state(message)


@setActionFor(GENERAL.START)
async def cmd_start_ad(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]

    if not db.userExists(cid):
        lang = DEFAULT_LANGUAGE
        db.query('INSERT INTO users (cid, name, joining_date, state_id, preferred_language)  VALUES (?, ?, ?, ?, ?)', (cid,message.from_user.full_name, utils.now(), GENERAL.START.ID, lang))
        await to_admin.new_user(message)

    if cid == ADMIN_CHAT_ID:
        await State.get(ADMIN.MENU)(message)
        return

    await ad_engine.sendAdTo(cid)

    if await checkForLink(message):
        logging.info(f"User {cid}:{message.from_user.full_name} used a link {message.text}")
    else:
        await State.get(USER.MAIN_MENU)(message, True)


async def checkForLink(message: types.Message) -> bool:
    cid, chat = message.chat.id, cm[message.chat.id]
    res = message.text.split(' ')
    
    if len(res) < 2:
        return False
    
    if res[0] == '/start':
        param = res[1]
        
    return False


@setActionFor(GENERAL.ERROR)
async def wrong_action(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]
    await chat.send (P.wrong_action(cid), temporary=True)

@setActionFor(GENERAL.LANGUAGE.CHOOSE)
async def cmd_language_(message: Message):
    cid = message.chat.id
    chat = cm[cid]

    langs = P.languages(cid,True)
    markup = Buttons(True)
    markup.add(langs[P.ARM],GENERAL.LANGUAGE.FINISH,P.ARM)
    markup.add(langs[P.RUS],GENERAL.LANGUAGE.FINISH,P.RUS)
    markup.add(langs[P.ENG],GENERAL.LANGUAGE.FINISH,P.ENG)

    langs_c = P.language_choose(cid,True)
    await chat.edit(langs_c[P.ARM]+'\n'+langs_c[P.RUS] +'\n'+langs_c[P.ENG], reply_markup=markup)
    await chat.setState(GENERAL.LANGUAGE.CHOOSE)


@setActionFor(GENERAL.LANGUAGE.FINISH)
async def choose_language(message: Message, lang):
    cid = message.chat.id
    chat = cm[cid]

    db.setUserLang(cid,lang)
    await chat.edit(P.language_set(cid))

    await State.get(USER.MAIN_MENU)(message)


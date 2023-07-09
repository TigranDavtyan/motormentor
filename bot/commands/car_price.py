import utils.utils as utils
from aiogram.types import Message, ChatActions
from buttons.buttons import *
from config import ADMIN_CHAT_ID, LOCATIONS
from loader import *
from notifications import to_admin
from phrases import phrases as P
from states.states import ADMIN, GENERAL, USER, State
from utils.logging import logging
from .car_engine import Car, XGBModel
import matplotlib.pyplot as plt
import os
import numpy as np
import io

logger = logging.getLogger()

@setActionFor(USER.CAR_PRICE.INFO)
async def menu_car_price(message: Message, data = None):
    cid,chat = message.chat.id,cm[message.chat.id]

    if data:
        column, data = data.split(':')
        db.query(f'UPDATE car_prices SET {column} = ? WHERE cid = ?;', (data, cid))

    markup = Buttons()
    
    user_car = Car(cid)
    lang = db.getUserLang(cid)
    
    markup.row([[user_car.getBrand(),USER.CAR_PRICE.BRAND],[user_car.getModel(),USER.CAR_PRICE.MODEL]])
    markup.row([[P.year(cid, user_car.year), USER.CAR_PRICE.YEAR],[P.mileage(cid, int(user_car.mileage)), USER.CAR_PRICE.MILEAGE]])

    markup.row([[user_car.getExteriorColor(lang), USER.CAR_PRICE.EXTERIOR_COLOR],[user_car.getBodyType(lang), USER.CAR_PRICE.BODY_TYPE]])
    markup.row([[user_car.getEngineType(lang), USER.CAR_PRICE.ENGINE_TYPE],[P.engine_size(cid, user_car.engine_size), USER.CAR_PRICE.ENGINE_SIZE]])
    markup.row([[user_car.getTransmission(lang), USER.CAR_PRICE.TRANSMISSION],[user_car.getDriveType(lang), USER.CAR_PRICE.DRIVE_TYPE]])
    markup.row([[user_car.getSteeringWheel(lang), USER.CAR_PRICE.STEERING_WHEEL],[user_car.getGasEquipment(lang), USER.CAR_PRICE.GAS_EQUIPMENT]])
    markup.row([[P.interior_color(cid, user_car.getInteriorColor(lang)), USER.CAR_PRICE.INTERIOR_COLOR],[P.interior_material(cid, user_car.getInteriorMaterial(lang)), USER.CAR_PRICE.INTERIOR_MATERIAL]])

    markup.add(P.calculate(lang), USER.CAR_PRICE.CALCULATE_PRICE)
    markup.add(P.calculate_by_year(lang), USER.CAR_PRICE.CALCULATE_PRICE_BY_YEAR)
    markup.add(P.calculate_by_mileage(lang), USER.CAR_PRICE.CALCULATE_PRICE_BY_MILEAGE)
    try:
        markup.addLink(P.search_for_cars(lang),USER.CAR_PRICE.INFO, link=user_car.getLink())
    except:
        pass

    markup.add(P.menu(lang), USER.MAIN_MENU)

    satisfaction = db.fetchone('''SELECT COUNT(*) AS total_count,SUM(CASE WHEN price % 100 = 0 THEN 1 ELSE 0 END) AS divisible_by_100_count FROM car_price_results;''')
    count = satisfaction[0]
    notsatisfied = int(satisfaction[1] / count * 100)
    satisfied = 100 - notsatisfied

    filled = int(round(satisfied/10))
    empty = 10 - filled

    await chat.edit(P.car_price_info(lang, filled * '█', empty * '░', satisfied), markup)
    await chat.setState(USER.CAR_PRICE.INFO)


@setActionFor(USER.CAR_PRICE.CALCULATE_PRICE_BY_YEAR)
async def car_calculate_by_year(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]
    await bot.send_chat_action(cid, ChatActions.TYPING)

    user_car = Car(cid)
    start = 2000
    end = 2022
    years = range(start,end+1)
    website = 'listam' if chat.getLoc() == 0 else 'myauto.ge'
    try:
        prices = user_car.calculateByYear(years, website).astype(int)
    except Exception as e:
        logger.error('Calculation error ' + str(e))
        await chat.send(P.calculation_not_possible(cid), temporary=True)
        return
    
    plt.figure(figsize=(13, 8))
    plt.plot(years, prices, linewidth=2)
    plt.xlabel(P.label_year(cid))
    plt.ylabel(P.label_price(cid))
    plt.title(P.calculate_by_year(cid)[1:])
    plt.grid(linestyle='-', linewidth=1.5)
    plt.xticks(years, years,rotation=45)

    min_price = int(np.floor(min(prices)/1000)*1000)
    max_price = int(np.ceil(max(prices)/1000)*1000)+1000
    price_labels = range(min_price,max_price, 1000)
    plt.yticks(price_labels, price_labels)

    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='jpeg')
    buffer.seek(0)
    
    await chat.send('', photo=buffer.getvalue(), temporary=True)
    del buffer
    plt.close()
    

@setActionFor(USER.CAR_PRICE.CALCULATE_PRICE_BY_MILEAGE)
async def car_calculate_by_mileage(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    await bot.send_chat_action(cid, ChatActions.TYPING)

    user_car = Car(cid)
    start = 0
    end = 300000
    step = 5000
    mileages = range(start, end+step, step)
    website = 'listam' if chat.getLoc() == 0 else 'myauto.ge'
    try:
        prices = user_car.calculateByMileage(mileages, website)
    except Exception as e:
        logger.error('Calculation error ' + str(e))
        await chat.send(P.calculation_not_possible(cid), temporary=True)
        return
    
    window_size = 10
    weights = np.ones(window_size) / window_size
    prices_avg = np.convolve(prices, weights, mode='valid')
    prices = np.concatenate((prices[:window_size-1], prices_avg)).astype(int)

    plt.figure(figsize=(13, 8))
    plt.plot(mileages, prices, linewidth=2)
    plt.xlabel(P.label_mileage(cid))
    plt.ylabel(P.label_price(cid))
    plt.title(P.calculate_by_mileage(cid)[1:])
    plt.grid(linestyle='-', linewidth=1.5)
    plt.xticks(mileages, mileages,rotation=90)

    min_price = int(np.floor(min(prices)/1000)*1000)
    max_price = int(np.ceil(max(prices)/1000)*1000)+1000
    price_labels = range(min_price, max_price, 1000)
    plt.yticks(price_labels, price_labels)

    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='jpeg')
    buffer.seek(0)

    await chat.send('', photo=buffer.getvalue(), temporary=True)
    del buffer
    plt.close()

@setActionFor(USER.CAR_PRICE.CALCULATE_PRICE)
async def car_calculate(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    user_car = Car(cid)
    loc = chat.getLoc()
    website = 'listam' if loc == 0 else 'myauto.ge'
    try:
        price = int(round(user_car.calculatePrice(website)))
    except Exception as e:
        logger.error('Calculation error ' + str(e))
        await chat.send(P.calculation_not_possible(cid), temporary=True)
        return
    
    user_car.price = price

    is_first_calculation = int(db.fetchone('SELECT count(*) FROM user_cars WHERE cid = ?', (cid,))[0]) == 0
    if is_first_calculation:
        user_car.save_user_car(cid)

    price_str = f'{price:,}'

    lang = db.getUserLang(cid)
    text = P.calculate_result_title(lang, '')
    
    if loc == LOCATIONS.ARM:
        text += P.result_arm(lang, price_str) + '\n'
    elif loc == LOCATIONS.GE:
        text += P.result_ge(lang, price_str) + '\n'

    sub = chat.getSubscriptionLevel()
    if sub == 0:
        if loc == LOCATIONS.ARM:
            text += P.result_ge_not_available(lang) + '\n\n'
        elif loc == LOCATIONS.GE:
            text += P.result_arm_not_available(lang) + '\n\n'
    else:
        if loc == LOCATIONS.ARM:
            other_price = f'{int(round(user_car.calculatePrice("myauto.ge"))):,}'
            text += P.result_ge(lang, other_price) + '\n\n'
        elif loc == LOCATIONS.GE:
            other_price = f'{int(round(user_car.calculatePrice("listam"))):,}'
            text += P.result_arm(lang, other_price) + '\n'

    
    if not message.from_user.is_bot:
        await chat.send(text, temporary=True)
    else:
        if loc == LOCATIONS.ARM:
            text += P.price_result_ask_arm(cid)
        elif loc == LOCATIONS.GE:
            text += P.price_result_ask_ge(cid)

        markup = Buttons()
        markup.add(P.yes(cid), USER.CAR_PRICE.CALCULATE_GOOD, price)
        markup.add(P.dont_know(cid), USER.CAR_PRICE.CALCULATE_DONT_KNOW, price)
        markup.add(P.my_price(cid), USER.CAR_PRICE.CALCULATE_OFFER_PRICE)
        await chat.send(text, markup, temporary=True)

@setActionFor(USER.CAR_PRICE.CALCULATE_GOOD)
async def car_calculate_good(message: Message, data):
    cid, chat = message.chat.id,cm[message.chat.id]

    user_car = Car(cid)
    user_car.price = float(data)
    website = 'listam' if chat.getLoc() == 0 else 'myauto.ge'
    user_car.save(cid, website)

    await chat.edit(message.text, reply_markup=Buttons(), message_id=message.message_id)
    await chat.send(P.thanks_for_opinion(cid), temporary=True)

@setActionFor(USER.CAR_PRICE.CALCULATE_DONT_KNOW)
async def car_calculate_dont_know(message: Message, data):
    cid, chat = message.chat.id,cm[message.chat.id]

    await chat.edit(message.text, reply_markup=Buttons(), message_id=message.message_id)
    await chat.send(P.thanks_for_opinion(cid), temporary=True)

@setActionFor(USER.CAR_PRICE.CALCULATE_OFFER_PRICE)
async def car_calculate_offer(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    await chat.setState(USER.CAR_PRICE.CALCULATE_OFFER_PRICE)
    await chat.send(P.my_price_offer(cid), Buttons(True), temporary=True)

@setActionFor(USER.CAR_PRICE.CALCULATE_OFFER_PRICE_HANDLE)
async def car_calculate_offer_handle(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    user_car = Car(cid)
    try:
        user_car.price = float(message.text)
    except:
        await chat.send(P.wrong_format(cid), temporary=True)
        return
    website = 'listam' if chat.getLoc() == 0 else 'myauto.ge'
    user_car.save(cid, website)

    await chat.send(P.thanks_for_opinion(cid), temporary=True)

@setActionFor(USER.CAR_PRICE.BRAND)
async def car_brand(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    for index, brand in XGBModel.getBrands():
        markup.add(brand, USER.CAR_PRICE.INFO, f'car_brand:{index}')

    await chat.edit(P.choose_car_brand(cid), markup)

    await chat.setState(USER.CAR_PRICE.BRAND)

@setActionFor(USER.CAR_PRICE.MODEL)
async def car_model(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    brand = db.fetchone('SELECT car_brand FROM car_prices WHERE cid = ?',(cid,))[0]

    markup = Buttons(True)
    for index, m in XGBModel.getModelsFor(brand):
        markup.add(m, USER.CAR_PRICE.INFO, f'model:{index}')

    await chat.edit(P.choose_car_model(cid), markup)

    await chat.setState(USER.CAR_PRICE.MODEL)

@setActionFor(USER.CAR_PRICE.EXTERIOR_COLOR)
async def car_exterior_color(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, color in XGBModel.getExteriorColors(lang):
        markup.add(color, USER.CAR_PRICE.INFO, f'exterior_color:{index}')

    await chat.edit(P.choose_car_exterior_color(cid), markup)

    await chat.setState(USER.CAR_PRICE.EXTERIOR_COLOR)

@setActionFor(USER.CAR_PRICE.BODY_TYPE)
async def car_body_type(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, body_type in XGBModel.getBodyTypes(lang):
        markup.add(body_type, USER.CAR_PRICE.INFO, f'body_type:{index}')

    await chat.edit(P.choose_car_body_type(cid), markup)

    await chat.setState(USER.CAR_PRICE.BODY_TYPE)

@setActionFor(USER.CAR_PRICE.ENGINE_TYPE)
async def car_engine_type(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, engine_type in XGBModel.getEngineTypes(lang):
        markup.add(engine_type, USER.CAR_PRICE.INFO, f'engine_type:{index}')

    await chat.edit(P.choose_car_engine_type(cid), markup)

    await chat.setState(USER.CAR_PRICE.ENGINE_TYPE)

@setActionFor(USER.CAR_PRICE.TRANSMISSION)
async def car_transmission(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, transmission in XGBModel.getTransmissions(lang):
        markup.add(transmission, USER.CAR_PRICE.INFO, f'transmission:{index}')

    await chat.edit(P.choose_car_transmission(cid), markup)

    await chat.setState(USER.CAR_PRICE.TRANSMISSION)

@setActionFor(USER.CAR_PRICE.DRIVE_TYPE)
async def car_drive_type(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, drive_type in XGBModel.getDriveTypes(lang):
        markup.add(drive_type, USER.CAR_PRICE.INFO, f'drive_type:{index}')

    await chat.edit(P.choose_car_drive_type(cid), markup)

    await chat.setState(USER.CAR_PRICE.DRIVE_TYPE)

@setActionFor(USER.CAR_PRICE.STEERING_WHEEL)
async def car_steering_wheel(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, steering_wheel in XGBModel.getSteeringWheels(lang):
        markup.add(steering_wheel, USER.CAR_PRICE.INFO, f'steering_wheel:{index}')

    await chat.edit(P.choose_car_steering_wheel(cid), markup)

    await chat.setState(USER.CAR_PRICE.STEERING_WHEEL)


@setActionFor(USER.CAR_PRICE.GAS_EQUIPMENT)
async def car_gas_equipment(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, gas_equipment in XGBModel.getGasEquipments(lang):
        markup.add(gas_equipment, USER.CAR_PRICE.INFO, f'gas_equipment:{index}')

    await chat.edit(P.choose_car_gas_equipment(cid), markup)

    await chat.setState(USER.CAR_PRICE.GAS_EQUIPMENT)

@setActionFor(USER.CAR_PRICE.INTERIOR_COLOR)
async def car_interior_color(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, interior_color in XGBModel.getInteriorColors(lang):
        markup.add(interior_color, USER.CAR_PRICE.INFO, f'interior_color:{index}')

    await chat.edit(P.choose_car_interior_color(cid), markup)

    await chat.setState(USER.CAR_PRICE.INTERIOR_COLOR)

@setActionFor(USER.CAR_PRICE.INTERIOR_MATERIAL)
async def car_interior_material(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, interior_material in XGBModel.getInteriorMaterials(lang):
        markup.add(interior_material, USER.CAR_PRICE.INFO, f'interior_material:{index}')

    await chat.edit(P.choose_car_interior_material(cid), markup)

    await chat.setState(USER.CAR_PRICE.INTERIOR_MATERIAL)


@setActionFor(USER.CAR_PRICE.YEAR)
async def car_year(message: Message, data=None):
    cid, chat = message.chat.id,cm[message.chat.id]
    if data:
        start_year = int(data)
    else:
        start_year = 2010

    markup = Buttons()
    
    markup.add('🔼', USER.CAR_PRICE.YEAR, start_year - 8)
    
    for year in range(start_year,start_year + 8):
        markup.add(str(year), USER.CAR_PRICE.INFO, f'year:{year}')
    
    markup.add('🔽', USER.CAR_PRICE.YEAR, start_year + 8)

    await chat.edit(P.choose_car_year(cid), markup)
    await chat.setState(USER.CAR_PRICE.YEAR)


@setActionFor(USER.CAR_PRICE.MILEAGE)
async def car_mileage(message: Message, data = None):
    cid, chat = message.chat.id,cm[message.chat.id]
    if data:
        start_mileage = int(data)
    else:
        start_mileage = 100000

    markup = Buttons()
    step = 5000
    markup.add('🔼', USER.CAR_PRICE.MILEAGE, start_mileage-step*8)
    
    for mileage in range(start_mileage, start_mileage+step*8, step):
        markup.add(P.mileage(cid, mileage), USER.CAR_PRICE.INFO, f'mileage:{mileage}')
    
    markup.add('🔽', USER.CAR_PRICE.MILEAGE, start_mileage+step*8)
    
    await chat.edit(P.choose_car_mileage(cid), markup)
    await chat.setState(USER.CAR_PRICE.MILEAGE)


@setActionFor(USER.CAR_PRICE.ENGINE_SIZE)
async def car_engine_size(message: Message, data = None):
    cid, chat = message.chat.id,cm[message.chat.id]

    if data:
        start_engine_size= float(data)
    else:
        start_engine_size = 1.0

    markup = Buttons()
    step = 0.8
    markup.add('🔼', USER.CAR_PRICE.ENGINE_SIZE, start_engine_size - step)
    
    for engine_size in np.arange(start_engine_size, start_engine_size + step, 0.1):
        engine_size = round(engine_size, 1)
        markup.add(f'{engine_size} L', USER.CAR_PRICE.INFO, f'engine_size:{engine_size}')
    
    markup.add('🔽', USER.CAR_PRICE.ENGINE_SIZE, start_engine_size + step)

    await chat.edit(P.choose_car_engine_size(cid), markup)
    await chat.setState(USER.CAR_PRICE.ENGINE_SIZE)



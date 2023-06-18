import utils.utils as utils
from aiogram.types import Message, ChatActions
from buttons.buttons import *
from config import ADMIN_CHAT_ID
from loader import *
from notifications import to_admin
from phrases import phrases as P
from states.states import ADMIN, GENERAL, USER, State
from utils.logging import logging
from .car_engine import SavedCar, model
import numpy as np
import asyncio
import json

@setActionFor(USER.SAVED.INFO)
async def saved_cars(message: Message):
    cid,chat = message.chat.id, cm[message.chat.id]

    saved_cars = db.fetchall('''SELECT id, car_brand, model,
        year, mileage_start, mileage_end, exterior_color, body_type, engine_type, engine_size,transmission,
        drive_type,condition, gas_equipment,steering_wheel, price_start, price_end, found_cars FROM saved_cars WHERE cid = ? AND editing = 0;''',(cid,))
    
    lang = db.getUserLang(cid)

    markup = Buttons()
    markup.add(P.add_saved_car(cid), USER.SAVED.ADD)
    markup.add(P.menu(cid), USER.MAIN_MENU)

    await chat.edit(P.saved_cars_info(cid), markup)
    await chat.setState(USER.SAVED.INFO)

    for car in saved_cars:
        id, car_brand, m, year, mileage_start, mileage_end, exterior_color, body_type, engine_type, engine_size,transmission,\
        drive_type,condition, gas_equipment,steering_wheel, price_start, price_end, found_cars = car
        
        saved_car = SavedCar(cid)
        saved_car.car_brand = car_brand;  saved_car.model = m
        saved_car.year = year;  saved_car.exterior_color = exterior_color
        saved_car.body_type = body_type;  saved_car.engine_type = engine_type
        saved_car.transmission = transmission;  saved_car.drive_type = drive_type
        saved_car.condition = condition;  saved_car.gas_equipment = gas_equipment
        saved_car.steering_wheel = steering_wheel

        found_cars = dict(json.loads(found_cars))

        description = f'''
<b>{saved_car.getBrand()} - {saved_car.getModel()} {engine_size}L</b>

<b>{P.year(lang, year)} {saved_car.getExteriorColor(lang)}</b>
{saved_car.getBodyType(lang)} {saved_car.getEngineType(lang)}
{saved_car.getTransmission(lang)} {saved_car.getDriveType(lang)}
{saved_car.getCondition(lang)} {saved_car.getGasEquipment(lang)}
{saved_car.getSteeringWheel(lang)}
<b>{int(mileage_start)} - {P.mileage(lang, int(mileage_end))}</b>
<b>{P.label_price(lang)}: {int(price_start)} - {int(price_end)}$</b>
'''
        nFound = len(found_cars)
        if nFound > 0:
            description += '\n'+P.found_cars_so_far(cid, nFound)

        for date, itemid in found_cars.items():
            description += f'\n{date} - list.am/item/{itemid}'

        markup = Buttons()
        markup.add(P.delete(cid), USER.SAVED.DELETE, str(id))

        await chat.send(description, markup, temporary=True)


@setActionFor(USER.SAVED.DELETE)
async def saved_car_delete(message: Message, data):
    cid, chat = message.chat.id, cm[message.chat.id]

    id = int(data)
    db.query('DELETE FROM saved_cars WHERE id=?', (id,))
    # await chat.send(P.deleted(cid), temporary=True)
    await bot.delete_message(cid, message.message_id)

@setActionFor(USER.SAVED.ADD)
async def saved_cars(message: Message, data = None):
    cid, chat = message.chat.id, cm[message.chat.id]

    if data:
        column, data = data.split(':')
        db.query(f'UPDATE saved_cars SET {column} = ? WHERE cid = ? AND editing = 1;', (data, cid))

    markup = Buttons()
    
    user_car = SavedCar(cid)
    lang = db.getUserLang(cid)
    
    markup.row([[user_car.getBrand(),USER.SAVED.CAR.BRAND],[user_car.getModel(),USER.SAVED.CAR.MODEL]])
    markup.row([[P.year(cid, user_car.year), USER.SAVED.CAR.YEAR],[user_car.getSteeringWheel(lang), USER.SAVED.CAR.STEERING_WHEEL]])

    markup.row([[user_car.getExteriorColor(lang), USER.SAVED.CAR.EXTERIOR_COLOR],[user_car.getBodyType(lang), USER.SAVED.CAR.BODY_TYPE]])
    markup.row([[user_car.getEngineType(lang), USER.SAVED.CAR.ENGINE_TYPE],[P.engine_size(cid, user_car.engine_size), USER.SAVED.CAR.ENGINE_SIZE]])
    markup.row([[user_car.getTransmission(lang), USER.SAVED.CAR.TRANSMISSION],[user_car.getDriveType(lang), USER.SAVED.CAR.DRIVE_TYPE]])
    markup.row([[user_car.getCondition(lang), USER.SAVED.CAR.CONDITION],[user_car.getGasEquipment(lang), USER.SAVED.CAR.GAS_EQUIPMENT]])

    markup.row([['>>'+P.mileage(cid, int(user_car.mileage_start)), USER.SAVED.CAR.MILEAGE_START],['<<'+P.mileage(cid, int(user_car.mileage_end)), USER.SAVED.CAR.MILEAGE_END]])
    
    markup.row([[f'>>{int(user_car.price_start)}$', USER.SAVED.CAR.PRICE_START],[f'<<{int(user_car.price_end)}$', USER.SAVED.CAR.PRICE_END]])
    markup.add(P.save_car(lang), USER.SAVED.CAR.SAVE)
    markup.add(P.menu(cid), USER.MAIN_MENU)

    await chat.edit(P.add_saved_car(cid), markup)
    await chat.setState(USER.SAVED.ADD)


@setActionFor(USER.SAVED.CAR.SAVE)
async def car_save(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    user_car = SavedCar(cid)
    user_car.save()
    await chat.send(P.car_saved(cid), temporary=True)
    await asyncio.sleep(1)
    await State.get(USER.SAVED.INFO)(message)


@setActionFor(USER.SAVED.CAR.BRAND)
async def car_brand(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    for index, brand in model.getBrands():
        markup.add(brand, USER.SAVED.ADD, f'car_brand:{index}')

    await chat.edit(P.choose_car_brand(cid), markup)

    await chat.setState(USER.SAVED.CAR.BRAND)

@setActionFor(USER.SAVED.CAR.MODEL)
async def car_model(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    brand = db.fetchone('SELECT car_brand FROM saved_cars WHERE cid = ?',(cid,))[0]

    markup = Buttons(True)
    for index, m in model.getModelsFor(brand):
        markup.add(m, USER.SAVED.ADD, f'model:{index}')

    await chat.edit(P.choose_car_model(cid), markup)

    await chat.setState(USER.SAVED.CAR.MODEL)

@setActionFor(USER.SAVED.CAR.EXTERIOR_COLOR)
async def car_exterior_color(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, color in model.getExteriorColors(lang):
        markup.add(color, USER.SAVED.ADD, f'exterior_color:{index}')

    await chat.edit(P.choose_car_exterior_color(cid), markup)

    await chat.setState(USER.SAVED.CAR.EXTERIOR_COLOR)

@setActionFor(USER.SAVED.CAR.BODY_TYPE)
async def car_body_type(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, body_type in model.getBodyTypes(lang):
        markup.add(body_type, USER.SAVED.ADD, f'body_type:{index}')

    await chat.edit(P.choose_car_body_type(cid), markup)

    await chat.setState(USER.SAVED.CAR.BODY_TYPE)

@setActionFor(USER.SAVED.CAR.ENGINE_TYPE)
async def car_engine_type(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, engine_type in model.getEngineTypes(lang):
        markup.add(engine_type, USER.SAVED.ADD, f'engine_type:{index}')

    await chat.edit(P.choose_car_engine_type(cid), markup)

    await chat.setState(USER.SAVED.CAR.ENGINE_TYPE)

@setActionFor(USER.SAVED.CAR.TRANSMISSION)
async def car_transmission(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, transmission in model.getTransmissions(lang):
        markup.add(transmission, USER.SAVED.ADD, f'transmission:{index}')

    await chat.edit(P.choose_car_transmission(cid), markup)

    await chat.setState(USER.SAVED.CAR.TRANSMISSION)

@setActionFor(USER.SAVED.CAR.DRIVE_TYPE)
async def car_drive_type(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, drive_type in model.getDriveTypes(lang):
        markup.add(drive_type, USER.SAVED.ADD, f'drive_type:{index}')

    await chat.edit(P.choose_car_drive_type(cid), markup)

    await chat.setState(USER.SAVED.CAR.DRIVE_TYPE)

@setActionFor(USER.SAVED.CAR.CONDITION)
async def car_condition(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, condition in model.getConditions(lang):
        markup.add(condition, USER.SAVED.ADD, f'condition:{index}')

    await chat.edit(P.choose_car_condition(cid), markup)

    await chat.setState(USER.SAVED.CAR.CONDITION)

@setActionFor(USER.SAVED.CAR.STEERING_WHEEL)
async def car_steering_wheel(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, steering_wheel in model.getSteeringWheels(lang):
        markup.add(steering_wheel, USER.SAVED.ADD, f'steering_wheel:{index}')

    await chat.edit(P.choose_car_steering_wheel(cid), markup)

    await chat.setState(USER.SAVED.CAR.STEERING_WHEEL)


@setActionFor(USER.SAVED.CAR.GAS_EQUIPMENT)
async def car_gas_equipment(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, gas_equipment in model.getGasEquipments(lang):
        markup.add(gas_equipment, USER.SAVED.ADD, f'gas_equipment:{index}')

    await chat.edit(P.choose_car_gas_equipment(cid), markup)

    await chat.setState(USER.SAVED.CAR.GAS_EQUIPMENT)


@setActionFor(USER.SAVED.CAR.YEAR)
async def car_year(message: Message, data=None):
    cid, chat = message.chat.id,cm[message.chat.id]
    if data:
        start_year = int(data)
    else:
        start_year = 2010

    markup = Buttons()
    
    markup.add('🔼', USER.SAVED.CAR.YEAR, start_year - 8)
    
    for year in range(start_year,start_year + 8):
        markup.add(str(year), USER.SAVED.ADD, f'year:{year}')
    
    markup.add('🔽', USER.SAVED.CAR.YEAR, start_year + 8)

    await chat.edit(P.choose_car_year(cid), markup)
    await chat.setState(USER.SAVED.CAR.YEAR)


@setActionFor(USER.SAVED.CAR.MILEAGE_START)
async def car_mileage_start(message: Message, data = None):
    cid, chat = message.chat.id,cm[message.chat.id]
    if data:
        start_mileage = int(data)
    else:
        start_mileage = 100000

    markup = Buttons()
    step = 5000
    markup.add('🔼', USER.SAVED.CAR.MILEAGE_START, start_mileage-step*8)
    
    for mileage in range(start_mileage, start_mileage+step*8, step):
        markup.add(P.mileage(cid, mileage), USER.SAVED.ADD, f'mileage_start:{mileage}')
    
    markup.add('🔽', USER.SAVED.CAR.MILEAGE_START, start_mileage+step*8)
    
    await chat.edit(P.choose_car_mileage_start(cid), markup)
    await chat.setState(USER.SAVED.CAR.MILEAGE_START)

@setActionFor(USER.SAVED.CAR.MILEAGE_END)
async def car_mileage_end(message: Message, data = None):
    cid, chat = message.chat.id,cm[message.chat.id]
    if data:
        start_mileage = int(data)
    else:
        start_mileage = 100000

    markup = Buttons()
    step = 5000
    markup.add('🔼', USER.SAVED.CAR.MILEAGE_END, start_mileage-step*8)
    
    for mileage in range(start_mileage, start_mileage+step*8, step):
        markup.add(P.mileage(cid, mileage), USER.SAVED.ADD, f'mileage_end:{mileage}')
    
    markup.add('🔽', USER.SAVED.CAR.MILEAGE_END, start_mileage+step*8)
    
    await chat.edit(P.choose_car_mileage_end(cid), markup)
    await chat.setState(USER.SAVED.CAR.MILEAGE_END)


@setActionFor(USER.SAVED.CAR.PRICE_START)
async def car_price_start(message: Message, data = None):
    cid, chat = message.chat.id,cm[message.chat.id]
    if data:
        start_price = int(data)
    else:
        start_price = 10000

    markup = Buttons()
    step = 500
    markup.add('🔼', USER.SAVED.CAR.PRICE_START, start_price-step*8)
    
    for price in range(start_price, start_price+step*8, step):
        markup.add(f'{price}$', USER.SAVED.ADD, f'price_start:{price}')
    
    markup.add('🔽', USER.SAVED.CAR.PRICE_START, start_price+step*8)
    
    await chat.edit(P.choose_car_price_start(cid), markup)
    await chat.setState(USER.SAVED.CAR.PRICE_START)

@setActionFor(USER.SAVED.CAR.PRICE_END)
async def car_price_end(message: Message, data = None):
    cid, chat = message.chat.id,cm[message.chat.id]
    if data:
        start_price = int(data)
    else:
        start_price = 10000

    markup = Buttons()
    step = 500
    markup.add('🔼', USER.SAVED.CAR.PRICE_END, start_price-step*8)
    
    for price in range(start_price, start_price+step*8, step):
        markup.add(f'{price}$', USER.SAVED.ADD, f'price_end:{price}')
    
    markup.add('🔽', USER.SAVED.CAR.PRICE_END, start_price+step*8)
    
    await chat.edit(P.choose_car_price_end(cid), markup)
    await chat.setState(USER.SAVED.CAR.PRICE_END)


@setActionFor(USER.SAVED.CAR.ENGINE_SIZE)
async def car_engine_size(message: Message, data = None):
    cid, chat = message.chat.id,cm[message.chat.id]

    if data:
        start_engine_size= float(data)
    else:
        start_engine_size = 1.0

    markup = Buttons()
    step = 0.8
    markup.add('🔼', USER.SAVED.CAR.ENGINE_SIZE, start_engine_size - step)
    
    for engine_size in np.arange(start_engine_size, start_engine_size + step, 0.1):
        engine_size = round(engine_size, 1)
        markup.add(f'{engine_size} L', USER.SAVED.ADD, f'engine_size:{engine_size}')
    
    markup.add('🔽', USER.SAVED.CAR.ENGINE_SIZE, start_engine_size + step)

    await chat.edit(P.choose_car_engine_size(cid), markup)
    await chat.setState(USER.SAVED.CAR.ENGINE_SIZE)

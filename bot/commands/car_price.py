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
from utils.logging import logging
import json
import os
import pickle
import pandas as pd

class Model:
    file = None
    mtime = None
    filename = '../trained_model/categorical.json'

    model = None
    mmodel = None
    model_filename = '../trained_model/xgb_model.pkl'

    encoder = None
    mencoder = None
    encoder_filename = '../trained_model/encoder.pkl'

    def __init__(self):
        if not Model.file:
            with open(Model.filename, 'r') as file:
                Model.file = json.load(file)
            Model.mtime = os.path.getmtime(Model.filename)

        if not Model.encoder:
            with open(Model.encoder_filename, 'rb') as file:
                Model.encoder = pickle.load(file)
            Model.mencoder = os.path.getmtime(Model.encoder_filename)

        if not Model.model:
            with open(Model.model_filename, 'rb') as file:
                Model.model = pickle.load(file)
            Model.mmodel = os.path.getmtime(Model.model_filename)

    def update(self):
        new_mtime = os.path.getmtime(Model.filename)
        if new_mtime > Model.mtime:
            Model.mtime = new_mtime
            with open(Model.filename, 'r') as file:
                Model.file = json.load(file)


        new_mtime = os.path.getmtime(Model.encoder_filename)
        if new_mtime > Model.mencoder:
            Model.mencoder = new_mtime
            with open(Model.encoder_filename, 'rb') as file:
                Model.encoder = pickle.load(file)


        new_mtime = os.path.getmtime(Model.model_filename)
        if new_mtime > Model.mmodel:
            Model.mmodel = new_mtime
            with open(Model.model_filename, 'rb') as file:
                Model.model = pickle.load(file)

    def getModel(self):
        return Model.model
    def getEncoder(self):
        return Model.encoder
    
    def getBrands(self):
        ret = []
        indexes = list(Model.file['brands'].keys())
        for index in indexes:
            name = index.replace('_',' ')
            name = name[0].upper() + name[1:]
            ret.append((index, name))

        return ret
    
    def getModelsFor(self, brand):
        ret = []
        models_or_brand = Model.file['brands'][brand]
        for index in models_or_brand:
            name = index.replace('_',' ')
            name = name[0].upper() + name[1:]
            ret.append((index,name))
        
        return ret
    
    def getExteriorColors(self, lang):
        colors = Model.file['exterior_color']
        return [(color,eval(f'P.exterior_{color}({lang})')) for color in colors]
    def getInteriorColors(self, lang):
        colors = Model.file['interior_color']
        return [(color,eval(f'P.interior_{color}({lang})')) for color in colors]

    def getInteriorMaterials(self, lang):
        materials = Model.file['interior_material']
        return [(material,eval(f'P.{material}({lang})')) for material in materials]

    def getBodyTypes(self, lang):
        body_types = Model.file['body_type']
        ret = []
        for body_type in body_types:
            _body_type = body_type
            if body_type.startswith('suv'):
                _body_type = 'crossover'
            ret.append((body_type,eval(f'P.{_body_type}({lang})')))
        return ret

    def getEngineTypes(self, lang):
        engine_types = Model.file['engine_type']
        return [(engine_type ,eval(f'P.{engine_type}({lang})')) for engine_type in engine_types]

    def getTransmissions(self, lang):
        transmissions = Model.file['transmission']
        return [(transmission ,eval(f'P.{transmission}({lang})')) for transmission in transmissions]


    def getDriveTypes(self, lang):
        drive_types = Model.file['drive_type']
        return [(drive_type ,eval(f'P.{drive_type}({lang})')) for drive_type in drive_types]
    def getConditions(self, lang):
        conditions = Model.file['condition']
        return [(condition ,eval(f'P.{condition}({lang})')) for condition in conditions]
    def getGasEquipments(self, lang):
        gas_equipments = Model.file['gas_equipment']
        return [(gas_equipment ,eval(f'P.gas_{gas_equipment}({lang})')) for gas_equipment in gas_equipments]


    def getSteeringWheels(self, lang):
        steering_wheels = Model.file['steering_wheel']
        return [(steering_wheel ,eval(f'P.{steering_wheel}_steering({lang})')) for steering_wheel in steering_wheels]
    def getHeadlights(self, lang):
        headlightss = Model.file['headlights']
        return [(headlights ,eval(f'P.{headlights}({lang})')) for headlights in headlightss]
    def getSunroofs(self, lang):
        sunroofs = Model.file['sunroof']
        return [(sunroof ,eval(f'P.{sunroof}_sunroof({lang})')) for sunroof in sunroofs]

model = Model()

class Car:
    def __init__(self, cid):
        car = db.fetchone('SELECT car_brand,model,year,mileage,exterior_color,body_type,engine_type,engine_size,transmission,drive_type,condition,gas_equipment,steering_wheel,headlights,interior_color,interior_material,sunroof,wheel_size,price FROM car_prices WHERE cid = ?',(cid,))

        if not car:
            db.query('''INSERT INTO car_prices (cid,car_brand,model,year,mileage,exterior_color,body_type,engine_type,engine_size,
                     transmission,drive_type,condition,gas_equipment,steering_wheel,headlights,interior_color,interior_material,sunroof,wheel_size,price)
                     VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,-1)''',(cid,'Toyota','camry',2020,50000,'white','sedan','gasoline',
                                                                           2.5, 'automatic', 'front_wheel_drive','car_is_not_damaged','no','left',
                                                                           'led_headlights','black','leather','no',17))
            car = db.fetchone('SELECT car_brand,model,year,mileage,exterior_color,body_type,engine_type,engine_size,transmission,drive_type,condition,gas_equipment,steering_wheel,headlights,interior_color,interior_material,sunroof,wheel_size,price FROM car_prices WHERE cid = ?',(cid,))

        self.car_brand = car[0]
        self.model = car[1]
        self.year = car[2]
        self.mileage = car[3]
        self.exterior_color = car[4]
        self.body_type = car[5]
        self.engine_type = car[6]
        self.engine_size = car[7]
        self.transmission = car[8]
        self.drive_type = car[9]
        self.condition = car[10]
        self.gas_equipment = car[11]
        self.steering_wheel = car[12]
        self.headlights = car[13]
        self.interior_color = car[14]
        self.interior_material = car[15]
        self.sunroof = car[16]
        self.wheel_size = car[17]
        self.price = car[18]

    def calculatePrice(self):
        car = {}
        car['car_brand'] = self.car_brand
        car['model'] = self.model

        car['year'] = self.year
        car['engine_size'] = self.engine_size
        car['engine_type'] = self.engine_type
        car['mileage'] = self.mileage
        car['body_type'] = self.body_type
        car['transmission'] = self.transmission
        car['drive_type'] = self.drive_type
        car['condition'] = self.condition
        car['gas_equipment'] = self.gas_equipment
        car['steering_wheel'] = self.steering_wheel
        car['exterior_color'] = self.exterior_color
        car['headlights'] = self.headlights
        car['interior_color'] = self.interior_color
        car['interior_material'] = self.interior_material
        car['sunroof'] = self.sunroof
        car['wheel_size'] = self.wheel_size

        encoder = model.getEncoder()
        # print(len(encoder.get_feature_names_out()),'-----',encoder.get_feature_names_out())

        new_car_data = pd.DataFrame(car,index = [0])
        # Encode categorical variables using the trained OneHotEncoder
        encoded_data = encoder.transform(new_car_data[['car_brand', 'model', 'body_type', 'engine_type', 'transmission', 'drive_type',
                                                            'condition', 'gas_equipment', 'steering_wheel', 'exterior_color',
                                                            'headlights', 'interior_color', 'interior_material', 'sunroof']]).toarray()

        
        # Create a DataFrame from the encoded data
        encoded_car_data = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out())

        # Concatenate the encoded data with the numerical columns
        new_car_data_encoded = pd.concat([new_car_data[['year', 'engine_size', 'mileage', 'wheel_size']], encoded_car_data], axis=1)

        # Make predictions on the new car data
        predictions = model.getModel().predict(new_car_data_encoded)

        return predictions[0]


    def getBrand(self):
        brand = self.car_brand.replace('_',' ')
        return brand[0].upper() + brand[1:]
    def getModel(self):
        model = self.model.replace('_',' ')
        return model[0].upper() + model[1:]
    def getExteriorColor(self, lang):
        return eval(f'P.exterior_{self.exterior_color}({lang})')
    def getBodyType(self, lang):
        body_type = self.body_type
        if self.body_type.startswith('suv'):
            body_type = 'crossover'
        return eval(f'P.{body_type}({lang})')
    def getEngineType(self,lang):
        return eval(f'P.{self.engine_type}({lang})')
    def getTransmission(self,lang):
        return eval(f'P.{self.transmission}({lang})')

    def getDriveType(self,lang):
        return eval(f'P.{self.drive_type}({lang})')
    def getCondition(self,lang):
        return eval(f'P.{self.condition}({lang})')
    def getSteeringWheel(self,lang):
        return eval(f'P.{self.steering_wheel}_steering({lang})')
    def getHeadlights(self,lang):
        return eval(f'P.{self.headlights}({lang})')
    def getInteriorColor(self,lang):
        return eval(f'P.interior_{self.interior_color}({lang})')
  
    def getGasEquipment(self,lang):
        return eval(f'P.gas_{self.gas_equipment}({lang})')

    def getInteriorMaterial(self,lang):
        return eval(f'P.{self.interior_material}({lang})')
    def getSunroof(self,lang):
        return eval(f'P.{self.sunroof}_sunroof({lang})')


@setActionFor(USER.CAR_PRICE.INFO)
async def menu_car_price(message: Message, data = None):
    cid,chat = message.chat.id,cm[message.chat.id]

    if data:
        column, data = data.split(':')
        db.query(f'UPDATE car_prices SET {column} = ? WHERE cid = ?;', (data, cid))

    markup = Buttons()
    
    user_car = Car(cid)
    lang = db.getUserLang(cid)
    markup.add(P.language_change(cid), GENERAL.LANGUAGE.CHOOSE)
    markup.row([[user_car.getBrand(),USER.CAR_PRICE.BRAND],[user_car.getModel(),USER.CAR_PRICE.MODEL]])
    markup.row([[P.year(cid, user_car.year), USER.CAR_PRICE.YEAR],[P.mileage(cid, int(user_car.mileage)), USER.CAR_PRICE.MILEAGE]])

    markup.row([[user_car.getExteriorColor(lang), USER.CAR_PRICE.EXTERIOR_COLOR],[user_car.getBodyType(lang), USER.CAR_PRICE.BODY_TYPE]])
    markup.row([[user_car.getEngineType(lang), USER.CAR_PRICE.ENGINE_TYPE],[P.engine_size(cid, user_car.engine_size), USER.CAR_PRICE.ENGINE_SIZE]])
    markup.row([[user_car.getTransmission(lang), USER.CAR_PRICE.TRANSMISSION],[user_car.getDriveType(lang), USER.CAR_PRICE.DRIVE_TYPE]])
    markup.row([[user_car.getCondition(lang), USER.CAR_PRICE.CONDITION],[user_car.getGasEquipment(lang), USER.CAR_PRICE.GAS_EQUIPMENT]])
    markup.row([[user_car.getSteeringWheel(lang), USER.CAR_PRICE.STEERING_WHEEL],[user_car.getHeadlights(lang), USER.CAR_PRICE.HEADLIGHTS]])
    markup.row([[P.interior_color(cid, user_car.getInteriorColor(lang)), USER.CAR_PRICE.INTERIOR_COLOR],[P.interior_material(cid, user_car.getInteriorMaterial(lang)), USER.CAR_PRICE.INTERIOR_MATERIAL]])
    markup.row([[user_car.getSunroof(lang), USER.CAR_PRICE.SUNROOF],[P.wheel_size(cid, int(user_car.wheel_size)), USER.CAR_PRICE.WHEEL_SIZE]])


    markup.add(P.calculate(cid), USER.CAR_PRICE.CALCULATE_PRICE)

    await chat.edit(P.car_price_info(cid), markup)
    await chat.setState(USER.CAR_PRICE.INFO)



@setActionFor(USER.CAR_PRICE.CALCULATE_PRICE)
async def car_calculate(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    user_car = Car(cid)
    price = int(round(user_car.calculatePrice()))
    price_dram = int(round(price * 385))
    price_rub = int(round(price * 79.7))

    await chat.send(P.calculate_result(cid, price, price_dram, price_rub), temporary=True)



@setActionFor(USER.CAR_PRICE.BRAND)
async def car_brand(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    for index, brand in model.getBrands():
        markup.add(brand, USER.CAR_PRICE.INFO, f'car_brand:{index}')

    await chat.edit(P.choose_car_brand(cid), markup)

    await chat.setState(USER.CAR_PRICE.BRAND)

@setActionFor(USER.CAR_PRICE.MODEL)
async def car_model(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    brand = db.fetchone('SELECT car_brand FROM car_prices WHERE cid = ?',(cid,))[0]

    markup = Buttons(True)
    for index, m in model.getModelsFor(brand):
        markup.add(m, USER.CAR_PRICE.INFO, f'model:{index}')

    await chat.edit(P.choose_car_model(cid), markup)

    await chat.setState(USER.CAR_PRICE.MODEL)


@setActionFor(USER.CAR_PRICE.EXTERIOR_COLOR)
async def car_exterior_color(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, color in model.getExteriorColors(lang):
        markup.add(color, USER.CAR_PRICE.INFO, f'exterior_color:{index}')

    await chat.edit(P.choose_car_exterior_color(cid), markup)

    await chat.setState(USER.CAR_PRICE.EXTERIOR_COLOR)


@setActionFor(USER.CAR_PRICE.BODY_TYPE)
async def car_body_type(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, body_type in model.getBodyTypes(lang):
        markup.add(body_type, USER.CAR_PRICE.INFO, f'body_type:{index}')

    await chat.edit(P.choose_car_body_type(cid), markup)

    await chat.setState(USER.CAR_PRICE.BODY_TYPE)


@setActionFor(USER.CAR_PRICE.ENGINE_TYPE)
async def car_engine_type(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, engine_type in model.getEngineTypes(lang):
        markup.add(engine_type, USER.CAR_PRICE.INFO, f'engine_type:{index}')

    await chat.edit(P.choose_car_engine_type(cid), markup)

    await chat.setState(USER.CAR_PRICE.ENGINE_TYPE)

@setActionFor(USER.CAR_PRICE.TRANSMISSION)
async def car_transmission(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, transmission in model.getTransmissions(lang):
        markup.add(transmission, USER.CAR_PRICE.INFO, f'transmission:{index}')

    await chat.edit(P.choose_car_transmission(cid), markup)

    await chat.setState(USER.CAR_PRICE.TRANSMISSION)

@setActionFor(USER.CAR_PRICE.DRIVE_TYPE)
async def car_drive_type(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, drive_type in model.getDriveTypes(lang):
        markup.add(drive_type, USER.CAR_PRICE.INFO, f'drive_type:{index}')

    await chat.edit(P.choose_car_drive_type(cid), markup)

    await chat.setState(USER.CAR_PRICE.DRIVE_TYPE)

@setActionFor(USER.CAR_PRICE.CONDITION)
async def car_condition(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, condition in model.getConditions(lang):
        markup.add(condition, USER.CAR_PRICE.INFO, f'condition:{index}')

    await chat.edit(P.choose_car_condition(cid), markup)

    await chat.setState(USER.CAR_PRICE.CONDITION)



@setActionFor(USER.CAR_PRICE.STEERING_WHEEL)
async def car_steering_wheel(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, steering_wheel in model.getSteeringWheels(lang):
        markup.add(steering_wheel, USER.CAR_PRICE.INFO, f'steering_wheel:{index}')

    await chat.edit(P.choose_car_steering_wheel(cid), markup)

    await chat.setState(USER.CAR_PRICE.STEERING_WHEEL)



@setActionFor(USER.CAR_PRICE.HEADLIGHTS)
async def car_headlights(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, headlights in model.getHeadlights(lang):
        markup.add(headlights, USER.CAR_PRICE.INFO, f'headlights:{index}')

    await chat.edit(P.choose_car_headlights(cid), markup)

    await chat.setState(USER.CAR_PRICE.HEADLIGHTS)



@setActionFor(USER.CAR_PRICE.GAS_EQUIPMENT)
async def car_gas_equipment(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, gas_equipment in model.getGasEquipments(lang):
        markup.add(gas_equipment, USER.CAR_PRICE.INFO, f'gas_equipment:{index}')

    await chat.edit(P.choose_car_gas_equipment(cid), markup)

    await chat.setState(USER.CAR_PRICE.GAS_EQUIPMENT)



@setActionFor(USER.CAR_PRICE.INTERIOR_COLOR)
async def car_interior_color(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, interior_color in model.getInteriorColors(lang):
        markup.add(interior_color, USER.CAR_PRICE.INFO, f'interior_color:{index}')

    await chat.edit(P.choose_car_interior_color(cid), markup)

    await chat.setState(USER.CAR_PRICE.INTERIOR_COLOR)




@setActionFor(USER.CAR_PRICE.INTERIOR_MATERIAL)
async def car_interior_material(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, interior_material in model.getInteriorMaterials(lang):
        markup.add(interior_material, USER.CAR_PRICE.INFO, f'interior_material:{index}')

    await chat.edit(P.choose_car_interior_material(cid), markup)

    await chat.setState(USER.CAR_PRICE.INTERIOR_MATERIAL)



@setActionFor(USER.CAR_PRICE.SUNROOF)
async def car_sunroof(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    markup = Buttons(True)
    lang = db.getUserLang(cid)

    for index, sunroof in model.getSunroofs(lang):
        markup.add(sunroof, USER.CAR_PRICE.INFO, f'sunroof:{index}')

    await chat.edit(P.choose_car_sunroof(cid), markup)

    await chat.setState(USER.CAR_PRICE.SUNROOF)


@setActionFor(USER.CAR_PRICE.YEAR)
async def car_year(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    await chat.setState(USER.CAR_PRICE.YEAR)
    await chat.send(P.choose_car_year(cid), temporary=True)

@setActionFor(USER.CAR_PRICE.YEAR_HANDLE)
async def car_year_handle(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    try:
        year = int(message.text)
    except:
        await chat.send(P.wrong_action(cid))
        return
    
    await State.get(USER.CAR_PRICE.INFO)(message, f'year:{year}')


@setActionFor(USER.CAR_PRICE.MILEAGE)
async def car_year(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    await chat.setState(USER.CAR_PRICE.MILEAGE)
    await chat.send(P.choose_car_mileage(cid), temporary=True)

@setActionFor(USER.CAR_PRICE.MILEAGE_HANDLE)
async def car_year_handle(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    try:
        mileage = int(message.text)
    except:
        await chat.send(P.wrong_action(cid))
        return
    
    await State.get(USER.CAR_PRICE.INFO)(message, f'mileage:{mileage}')


@setActionFor(USER.CAR_PRICE.ENGINE_SIZE)
async def car_year(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    await chat.setState(USER.CAR_PRICE.ENGINE_SIZE)
    await chat.send(P.choose_car_engine_size(cid), temporary=True)

@setActionFor(USER.CAR_PRICE.ENGINE_SIZE_HANDLE)
async def car_year_handle(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    try:
        engine_size = float(message.text)
    except:
        await chat.send(P.wrong_action(cid),temporary=True)
        return
    
    await State.get(USER.CAR_PRICE.INFO)(message, f'engine_size:{engine_size}')
    


@setActionFor(USER.CAR_PRICE.WHEEL_SIZE)
async def car_year(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    await chat.setState(USER.CAR_PRICE.WHEEL_SIZE)
    await chat.send(P.choose_car_wheel_size(cid), temporary=True)

@setActionFor(USER.CAR_PRICE.WHEEL_SIZE_HANDLE)
async def car_year_handle(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    try:
        wheel_size = int(message.text)
    except:
        await chat.send(P.wrong_action(cid))
        return
    
    await State.get(USER.CAR_PRICE.INFO)(message, f'wheel_size:{wheel_size}')


























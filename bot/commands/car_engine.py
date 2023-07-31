import json
import os
import pickle

import listamids
import pandas as pd
from loader import db
from phrases import phrases as P
from datetime import datetime
import numpy as np

excise_rate_year = {0:1.5, 1:1.5, 2:1.5, 3:1.4, 4:1.2, 5:1, 6:0.8, 7:0.8, 8:0.8, 9:0.9, 10:1.1, 11:1.3, 12:1.5, 13:1.8, 14:2.1, 'above':2.4}
def calc_excise_duty(cubic_capacity, age, left_wheel, lm = 1, hm = 3):
    excise_rate = excise_rate_year[age] if age in excise_rate_year.keys() else excise_rate_year['above']
    
    return excise_rate * cubic_capacity * (lm if left_wheel else hm)
        
def calculate_import_tax(cubic_capacity, age):
    import_tax = np.ceil((cubic_capacity * 0.05) + (cubic_capacity * age * 0.0025))
    return import_tax

class File:
    def __init__(self, filename):
        self.filename = filename
        self.modified_time = os.path.getmtime(self.filename)
        self.file = None
        self.open()

    def open(self):
        extention = self.filename.split('.')[-1]
        if extention == 'json':
            with open(self.filename, 'r') as file:
                self.file = json.load(file)

        elif extention == 'pkl':
            with open(self.filename, 'rb') as file:
                self.file = pickle.load(file)

        else:
            with open(self.filename, 'r') as file:
                self.file = file

    def update(self):
        new_mtime = os.path.getmtime(self.filename)
        if new_mtime > self.modified_time:
            self.open()

class Model:
    def __init__(self):
        self.categorical = File(f'../trained_models/combined/categorical.json')
        self.model = File(f'../trained_models/combined/xgb_model.pkl')
        self.encoder = File(f'../trained_models/combined/encoder.pkl')

    def update(self):
        self.categorical.update()
        self.model.update()
        self.encoder.update()

    def predictOne(self, car):
        new_car_data = pd.DataFrame(car, index = [0])

        encoder = self.encoder.file
        encoded_data = encoder.transform(new_car_data[['website','car_brand', 'model', 'body_type', 'engine_type', 'transmission', 'drive_type',
                                                            'gas_equipment', 'steering_wheel', 'exterior_color', 'interior_color', 'interior_material']]).toarray()

        encoded_car_data = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out())
        new_car_data_encoded = pd.concat([new_car_data[['year', 'engine_size', 'mileage']], encoded_car_data], axis=1)

        predictions = self.model.file.predict(new_car_data_encoded)

        return predictions[0]

    def getModel(self):
        return self.model.file

    def getEncoder(self):
        return self.encoder.file

    def getBrands(self):
        ret = []
        indexes = list(self.categorical.file['brands'].keys())
        for index in indexes:
            name = index.replace('_',' ')
            name = name[0].upper() + name[1:]
            ret.append((index, name))

        return ret
    
    def getModelsFor(self, brand):
        ret = []
        models_or_brand = self.categorical.file['brands'][brand]
        for index in models_or_brand:
            name = index.replace('_',' ')
            name = name[0].upper() + name[1:]
            ret.append((index,name))
        
        return ret
    
    def getExteriorColors(self, lang):
        colors = self.categorical.file['exterior_color']
        return [(color,eval(f'P.exterior_{color}({lang})')) for color in colors]
    def getInteriorColors(self, lang):
        colors = self.categorical.file['interior_color']
        return [(color,eval(f'P.interior_{color}({lang})')) for color in colors]

    def getInteriorMaterials(self, lang):
        materials = self.categorical.file['interior_material']
        return [(material,eval(f'P.{material}({lang})')) for material in materials]

    def getBodyTypes(self, lang):
        body_types = self.categorical.file['body_type']
        ret = []
        for body_type in body_types:
            _body_type = body_type
            if body_type.startswith('suv'):
                _body_type = 'crossover'
            ret.append((body_type,eval(f'P.{_body_type}({lang})')))
        return ret

    def getEngineTypes(self, lang):
        engine_types = self.categorical.file['engine_type']
        return [(engine_type ,eval(f'P.{engine_type}({lang})')) for engine_type in engine_types]

    def getTransmissions(self, lang):
        transmissions = self.categorical.file['transmission']
        return [(transmission ,eval(f'P.{transmission}({lang})')) for transmission in transmissions]

    def getDriveTypes(self, lang):
        drive_types = self.categorical.file['drive_type']
        return [(drive_type ,eval(f'P.{drive_type}({lang})')) for drive_type in drive_types]

    def getGasEquipments(self, lang):
        gas_equipments = self.categorical.file['gas_equipment']
        return [(gas_equipment ,eval(f'P.gas_{gas_equipment}({lang})')) for gas_equipment in gas_equipments]

    def getSteeringWheels(self, lang):
        steering_wheels = self.categorical.file['steering_wheel']
        return [(steering_wheel ,eval(f'P.{steering_wheel}_steering({lang})')) for steering_wheel in steering_wheels]

XGBModel = Model()

class Car:
    def __init__(self, cid = None, df_item = None, properties = None):
        if not cid:
            return
        if not df_item and properties:
            df_item = properties
        car = db.fetchone('SELECT car_brand,model,year,mileage,exterior_color,body_type,engine_type,engine_size,transmission,drive_type,gas_equipment,steering_wheel,interior_color,interior_material,price FROM car_prices WHERE cid = ?',(cid,))
        if df_item is not None:
            df_item = dict(df_item)
            for column in df_item.keys():
                if pd.isna(df_item[column]):
                    if column in default_car.keys():
                        df_item[column] = default_car[column]

            if not car:
                db.query('''INSERT INTO car_prices (cid,car_brand,model,year,mileage,exterior_color,body_type,engine_type,engine_size,
                    transmission,drive_type,gas_equipment,steering_wheel,interior_color,interior_material,price)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(cid,df_item['car_brand'],df_item['model'],df_item['year'],df_item['mileage'],
                                                                        df_item['exterior_color'],df_item['body_type'],df_item['engine_type'],
                                                                        df_item['engine_size'], df_item['transmission'], df_item['drive_type'],
                                                                        df_item['gas_equipment'],df_item['steering_wheel'],
                                                                        df_item['interior_color'],df_item['interior_material'], df_item['dollar_price']))
            else:
                db.query('''UPDATE car_prices SET car_brand=?,model=?,year=?,mileage=?,exterior_color=?,body_type=?,engine_type=?,engine_size=?,
                    transmission=?,drive_type=?,gas_equipment=?,steering_wheel=?,interior_color=?,interior_material=?,price=? WHERE cid=?''',
                                                                        (df_item['car_brand'],df_item['model'],df_item['year'],df_item['mileage'],
                                                                        df_item['exterior_color'],df_item['body_type'],df_item['engine_type'],
                                                                        df_item['engine_size'], df_item['transmission'], df_item['drive_type'],
                                                                        df_item['gas_equipment'],df_item['steering_wheel'],
                                                                        df_item['interior_color'],df_item['interior_material'],
                                                                        df_item['dollar_price'], cid))
        elif not car:
            db.query('''INSERT INTO car_prices (cid,car_brand,model,year,mileage,exterior_color,body_type,engine_type,engine_size,
                        transmission,drive_type,gas_equipment,steering_wheel,interior_color,interior_material,price)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,-1)''',(cid,'Toyota','camry',2020,50000,'white','sedan','gasoline',
                                                                            2.5, 'automatic', 'front_wheel_drive','no','left',
                                                                            'black','leather'))
            
        car = db.fetchone('SELECT car_brand,model,year,mileage,exterior_color,body_type,engine_type,engine_size,transmission,drive_type,gas_equipment,steering_wheel,interior_color,interior_material,price FROM car_prices WHERE cid = ?',(cid,))

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
        self.gas_equipment = car[10]
        self.steering_wheel = car[11]
        self.interior_color = car[12]
        self.interior_material = car[13]
        self.price = car[14]

    def save_user_car(self, cid):
        db.query('''INSERT INTO user_cars (cid,car_brand,model,year,mileage,exterior_color,body_type,engine_type,engine_size,
                     transmission,drive_type,gas_equipment,steering_wheel,interior_color,interior_material,price)
                     VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(cid,self.car_brand,self.model,self.year,self.mileage,self.exterior_color,
                                                                           self.body_type,self.engine_type,
                                                                           self.engine_size, self.transmission, self.drive_type,
                                                                           self.gas_equipment,self.steering_wheel,
                                                                           self.interior_color,self.interior_material,self.price))

    def save(self, cid, website):
        db.query('''INSERT INTO car_price_results (cid, website, car_brand,model,year,mileage,exterior_color,body_type,engine_type,engine_size,
                     transmission,drive_type,gas_equipment,steering_wheel,interior_color,interior_material,price)
                     VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(cid, website, self.car_brand,self.model,self.year,self.mileage,self.exterior_color,
                                                                           self.body_type,self.engine_type,
                                                                           self.engine_size, self.transmission, self.drive_type,
                                                                           self.gas_equipment,self.steering_wheel,
                                                                           self.interior_color,self.interior_material,self.price))
    def calculatePrice(self, website = 'listam') -> float:
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
        car['gas_equipment'] = self.gas_equipment
        car['steering_wheel'] = self.steering_wheel
        car['exterior_color'] = self.exterior_color
        car['interior_color'] = self.interior_color
        car['interior_material'] = self.interior_material
        car['website'] = website

        return XGBModel.predictOne(car)

    def calculateByYear(self, years, website = 'listam'):
        cars = []
        car = {}
        car['car_brand'] = self.car_brand
        car['model'] = self.model
        car['engine_size'] = self.engine_size
        car['engine_type'] = self.engine_type
        car['mileage'] = self.mileage
        car['body_type'] = self.body_type
        car['transmission'] = self.transmission
        car['drive_type'] = self.drive_type
        car['gas_equipment'] = self.gas_equipment
        car['steering_wheel'] = self.steering_wheel
        car['exterior_color'] = self.exterior_color
        car['interior_color'] = self.interior_color
        car['interior_material'] = self.interior_material
        car['website'] = website
        for year in years:
            c = car.copy()
            c['year'] = year
            cars.append(c)

        encoder = XGBModel.getEncoder()

        new_car_data = pd.DataFrame(cars,index = years)

        encoded_data = encoder.transform(new_car_data[['website', 'car_brand', 'model', 'body_type', 'engine_type', 'transmission', 'drive_type',
                                                            'gas_equipment', 'steering_wheel', 'exterior_color', 'interior_color','interior_material']]).toarray()

        encoded_car_data = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(), index  = years)
        new_car_data_encoded = pd.concat([new_car_data[['year', 'engine_size', 'mileage']], encoded_car_data], axis=1)

        predictions = XGBModel.getModel().predict(new_car_data_encoded)
        return predictions

    def calculateByMileage(self, mileages, website = 'listam'):
        cars = []
        car = {}
        car['car_brand'] = self.car_brand
        car['model'] = self.model
        car['year'] = self.year
        car['engine_size'] = self.engine_size
        car['engine_type'] = self.engine_type
        
        car['body_type'] = self.body_type
        car['transmission'] = self.transmission
        car['drive_type'] = self.drive_type
        car['gas_equipment'] = self.gas_equipment
        car['steering_wheel'] = self.steering_wheel
        car['exterior_color'] = self.exterior_color
        car['interior_color'] = self.interior_color
        car['interior_material'] = self.interior_material
        car['website'] = website

        for mileage in mileages:
            c = car.copy()
            c['mileage'] = mileage
            cars.append(c)
        
        encoder = XGBModel.getEncoder()

        new_car_data = pd.DataFrame(cars,index = mileages)

        encoded_data = encoder.transform(new_car_data[['website', 'car_brand', 'model', 'body_type', 'engine_type', 'transmission', 'drive_type',
                                                            'gas_equipment', 'steering_wheel', 'exterior_color', 'interior_color', 'interior_material']]).toarray()

        encoded_car_data = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(), index = mileages)
        new_car_data_encoded = pd.concat([new_car_data[['year', 'engine_size', 'mileage']], encoded_car_data], axis=1)

        predictions = XGBModel.getModel().predict(new_car_data_encoded)
        return predictions

    def calculateImportTax(self, website = 'listam'):
        if website == 'myauto.ge':
            left_wheel = self.steering_wheel == 'left'

            cubic_capacity = self.engine_size*1000
            if self.engine_type == 'electric':
                if left_wheel: cubic_capacity = 0 
                else: cubic_capacity = 2000 

            age = datetime.now().year - self.year

            excise_duty = calc_excise_duty(cubic_capacity, age, left_wheel, 0.4 if self.engine_type == 'hybrid' else 1)

            customs_service_tax = 150
            decoration = 200
            import_tax = calculate_import_tax(cubic_capacity, age)
            expert_assessment = 30
            customs_declaration = 50
            internal_transit = 50

            total = excise_duty + customs_service_tax + decoration + import_tax + expert_assessment + customs_declaration + internal_transit
            return round(total * 0.39) #lari to dollar rate
        
        else: return 0

    def getLink(self):
        brand_data = listamids.brand_ids[self.car_brand]
        brand = brand_data['id']
        model = brand_data['models'][self.model]
        body_type = listamids.body_types[self.body_type]
        start_year = self.year
        end_year = self.year
        engine_type = listamids.engine_types[self.engine_type]
        engine_size = self.engine_size
        transmission = listamids.transmissions[self.transmission]
        drive_type = listamids.drive_types[self.drive_type]

        mileage_start = self.mileage-10000
        mileage_end = self.mileage+10000

        gas_equipment = listamids.gas_equipments[self.gas_equipment]
        steering_wheel = listamids.steering_wheels[self.steering_wheel]
        exterior_color = listamids.exterior_colors[self.exterior_color]

        link = f'''https://www.list.am/category/23?n=0&bid={brand}&mid={model}&crc=&_a27={body_type}&_a2_1={start_year}&_a2_2={end_year}&_a15={engine_type}
        &_a28_1={engine_size}&_a28_2=&_a13={transmission}&_a23={drive_type}&_a1_1={mileage_start}&_a1_2={mileage_end}&_a43={gas_equipment}
        &_a16={steering_wheel}&_a17=1&_a22={exterior_color}&_a106=0&_a102=0&_a103=0&_a104=0'''
        
        return link

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
    def getSteeringWheel(self,lang):
        return eval(f'P.{self.steering_wheel}_steering({lang})')
    def getInteriorColor(self,lang):
        return eval(f'P.interior_{self.interior_color}({lang})')
    def getGasEquipment(self,lang):
        return eval(f'P.gas_{self.gas_equipment}({lang})')
    def getInteriorMaterial(self,lang):
        return eval(f'P.{self.interior_material}({lang})')


default_car = {
    'car_brand' : 'Toyota',
    'model' : 'camry',
    'year' : 2020,
    'engine_size' : 2.5,
    'engine_type' : 'gasoline',
    'mileage' : 50000,
    'body_type' : 'sedan',
    'transmission' : 'automatic',
    'drive_type' : 'front_wheel_drive',
    'gas_equipment' : 'no',
    'steering_wheel' : 'left',
    'exterior_color' : 'white',
    'interior_color' : 'black',
    'interior_material' : 'leather',
    'price' : 10000
   }


class SavedCar (Car):
    def __init__(self, cid):
        car = db.fetchone('''SELECT car_brand,model,year,mileage_start, mileage_end,exterior_color,body_type,
                          engine_type,engine_size,transmission,drive_type,gas_equipment,steering_wheel,price_start, 
                          price_end FROM saved_cars WHERE cid = ? AND editing = 1''',(cid,))
        if not car:
            db.query('''INSERT INTO saved_cars (cid, car_brand,model,year,mileage_start, mileage_end, exterior_color,body_type,engine_type,engine_size,
                        transmission,drive_type,gas_equipment,steering_wheel, price_start, price_end, found_cars)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, '[]')''',(cid,default_car['car_brand'],default_car['model'],default_car['year'],default_car['mileage']-5000, default_car['mileage']+5000,
                                                                        default_car['exterior_color'],default_car['body_type'],default_car['engine_type'],
                                                                        default_car['engine_size'], default_car['transmission'], default_car['drive_type'],
                                                                        default_car['gas_equipment'],default_car['steering_wheel'],default_car['price']-500,default_car['price']+500))
            car = db.fetchone('SELECT car_brand,model,year,mileage_start, mileage_end,exterior_color,body_type,engine_type,engine_size,transmission,drive_type,gas_equipment,steering_wheel,price_start, price_end FROM saved_cars WHERE cid = ? AND editing = 1',(cid,))

        self.cid = cid
        self.car_brand = car[0]
        self.model = car[1]
        self.year = car[2]
        self.mileage_start = car[3]
        self.mileage_end = car[4]
        self.exterior_color = car[5]
        self.body_type = car[6]
        self.engine_type = car[7]
        self.engine_size = car[8]
        self.transmission = car[9]
        self.drive_type = car[10]
        self.gas_equipment = car[11]
        self.steering_wheel = car[12]
        self.price_start = car[13]
        self.price_end = car[14]

    def save(self):
        db.query('UPDATE saved_cars SET editing=0 WHERE cid = ? and editing = 1', (self.cid,))
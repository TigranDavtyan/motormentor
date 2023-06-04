import os
import json
import pickle
import pandas as pd
from loader import db
from phrases import phrases as P

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

    data = None
    mdata = None
    data_filename = '../ForSale/Cars/listings.csv'

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

        if not Model.data:
            Model.data = pd.read_csv(Model.data_filename)
            Model.data.set_index('itemid', inplace=True)
            Model.mdata = os.path.getmtime(Model.data_filename)

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

        new_mtime = os.path.getmtime(Model.data_filename)
        if new_mtime > Model.mdata:
            Model.mdata = new_mtime
            Model.data = pd.read_csv(Model.data_filename)
            Model.data.set_index('itemid', inplace=True)

    def getModel(self):
        return Model.model
    def getEncoder(self):
        return Model.encoder
    def getData(self):
        return Model.data

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
    'condition' : 'car_is_not_damaged',
    'gas_equipment' : 'no',
    'steering_wheel' : 'left',
    'exterior_color' : 'white',
    'headlights' : 'led_headlights',
    'interior_color' : 'black',
    'interior_material' : 'leather',
    'sunroof' : 'no',
    'wheel_size' : 17
   }

class Car:
    def __init__(self, cid, df_item = None):
        car = db.fetchone('SELECT car_brand,model,year,mileage,exterior_color,body_type,engine_type,engine_size,transmission,drive_type,condition,gas_equipment,steering_wheel,headlights,interior_color,interior_material,sunroof,wheel_size,price FROM car_prices WHERE cid = ?',(cid,))
        if df_item is not None:
            for column in df_item.keys():
                if pd.isna(df_item[column]):
                    if column in default_car.keys():
                        df_item[column] = default_car[column]
                        
            if not car:
                db.query('''INSERT INTO car_prices (cid,car_brand,model,year,mileage,exterior_color,body_type,engine_type,engine_size,
                    transmission,drive_type,condition,gas_equipment,steering_wheel,headlights,interior_color,interior_material,sunroof,wheel_size,price)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(cid,df_item['car_brand'],df_item['model'],df_item['year'],df_item['mileage'],
                                                                        df_item['exterior_color'],df_item['body_type'],df_item['engine_type'],
                                                                        df_item['engine_size'], df_item['transmission'], df_item['drive_type'],
                                                                        df_item['condition'],df_item['gas_equipment'],df_item['steering_wheel'],
                                                                        df_item['headlights'],df_item['interior_color'],df_item['interior_material'],
                                                                        df_item['sunroof'],df_item['wheel_size'],df_item['dollar_price']))
            else:
                db.query('''UPDATE car_prices SET car_brand=?,model=?,year=?,mileage=?,exterior_color=?,body_type=?,engine_type=?,engine_size=?,
                    transmission=?,drive_type=?,condition=?,gas_equipment=?,steering_wheel=?,headlights=?,interior_color=?,interior_material=?,sunroof=?,wheel_size=?,price=? WHERE cid=?''',
                                                                        (df_item['car_brand'],df_item['model'],df_item['year'],df_item['mileage'],
                                                                        df_item['exterior_color'],df_item['body_type'],df_item['engine_type'],
                                                                        df_item['engine_size'], df_item['transmission'], df_item['drive_type'],
                                                                        df_item['condition'],df_item['gas_equipment'],df_item['steering_wheel'],
                                                                        df_item['headlights'],df_item['interior_color'],df_item['interior_material'],
                                                                        df_item['sunroof'],df_item['wheel_size'],df_item['dollar_price'], cid))
        elif not car:
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

    def save_user_car(self, cid):
        db.query('''INSERT INTO user_cars (cid,car_brand,model,year,mileage,exterior_color,body_type,engine_type,engine_size,
                     transmission,drive_type,condition,gas_equipment,steering_wheel,headlights,interior_color,interior_material,sunroof,wheel_size,price)
                     VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(cid,self.car_brand,self.model,self.year,self.mileage,self.exterior_color,
                                                                           self.body_type,self.engine_type,
                                                                           self.engine_size, self.transmission, self.drive_type,
                                                                           self.condition,self.gas_equipment,self.steering_wheel,
                                                                           self.headlights,self.interior_color,self.interior_material,self.sunroof,self.wheel_size,self.price))

    def save(self, cid):
        db.query('''INSERT INTO car_price_results (cid,car_brand,model,year,mileage,exterior_color,body_type,engine_type,engine_size,
                     transmission,drive_type,condition,gas_equipment,steering_wheel,headlights,interior_color,interior_material,sunroof,wheel_size,price)
                     VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(cid,self.car_brand,self.model,self.year,self.mileage,self.exterior_color,
                                                                           self.body_type,self.engine_type,
                                                                           self.engine_size, self.transmission, self.drive_type,
                                                                           self.condition,self.gas_equipment,self.steering_wheel,
                                                                           self.headlights,self.interior_color,self.interior_material,self.sunroof,self.wheel_size,self.price))
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

        new_car_data = pd.DataFrame(car,index = [0])
        # Encode categorical variables using the trained OneHotEncoder
        encoded_data = encoder.transform(new_car_data[['car_brand', 'model', 'body_type', 'engine_type', 'transmission', 'drive_type',
                                                            'condition', 'gas_equipment', 'steering_wheel', 'exterior_color',
                                                            'headlights', 'interior_color', 'interior_material', 'sunroof']]).toarray()

        encoded_car_data = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out())
        new_car_data_encoded = pd.concat([new_car_data[['year', 'engine_size', 'mileage', 'wheel_size']], encoded_car_data], axis=1)

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

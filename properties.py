from bidict import bidict
import logging
logger = logging.getLogger('listamscraper')


def default_func(val):
    # logger.error(f'Dont have corresponding value for {val}')
    return val

def milage(val):
    number, type = val.replace(',','').split('_')
    number = int(number)
    if type == 'km':
        return number
    else:
        return number * 1.60934

class property:
    def __init__(self, dict: bidict, func = default_func):
        self.bidict = dict
        self.func = func

    def get(self, val) -> int:
        if val in self.bidict.keys():
            return self.bidict[val]
        else:
            return self.func(val)

    def inverse(self, val) -> str:
        if val in self.bidict.inverse.keys():
            return self.bidict.inverse[val]
        else:
            return val


class CarProperties:
    default                  = property(bidict({}), default_func )
    itemid                   = property(bidict({}), lambda val: int(val))
    car_brand                = property(bidict({}))
    model                 = property(bidict({}))
    body_type        = property(bidict({}))
    year                 = property(bidict({}), lambda val: int(val))
    engine_type                 = property(bidict({}))
    engine_size                 = property(bidict({}), lambda val: float(val.split('_')[0]))
    transmission                 = property(bidict({}))

    drive_type                 = property(bidict({}))
    mileage                 = property(bidict({}), milage)
    condition                 = property(bidict({}))
    gas_equipment                 = property(bidict({}))
    steering_wheel                 = property(bidict({}))
    cleared_customs                 = property(bidict({}))

    exterior_color                 = property(bidict({}))
    headlights                 = property(bidict({}))
    interior_color                 = property(bidict({}))
    interior_material                 = property(bidict({}))
    sunroof                 = property(bidict({}))
    wheel_size                 = property(bidict({}), lambda val: int(val.replace('r','')))

    # wheel_size                 = property(bidict({}))
    # wheel_size                 = property(bidict({}))
    # wheel_size                 = property(bidict({}))
    # wheel_size                 = property(bidict({}))

    # wheel_size                 = property(bidict({}))
    # wheel_size                 = property(bidict({}))
    # wheel_size                 = property(bidict({}))


    dollar_price             = property( bidict({}),lambda val : int(val.replace(',',''))  if val else None)
    dram_price               = property( bidict({}),lambda val : int(val.replace(',',''))  if val else None)
    ruble_price              = property( bidict({}),lambda val : int(val.replace(',',''))  if val else None)

    userid                   = property( bidict({}),lambda val : int(val)  if val else None)
    posted_date              = property( bidict({}),lambda val : val if val else None)
    update_date              = property( bidict({}),lambda val : val if val else None)
    closed_item              = property( bidict({}),lambda val : val if val else None)

    @staticmethod
    def get(key, value) -> int:
        return getattr(CarProperties, key, CarProperties.default).get(value)
    
    @staticmethod
    def inverseGet(value, key):
        return getattr(CarProperties, key, CarProperties.default).inverse(value)
    
    @staticmethod
    def getColumnNames():
        columns = []
        for name, obj in CarProperties.__dict__.items():
            if type(obj) is property:
                if name != 'default':
                    columns.append(name)
        return columns

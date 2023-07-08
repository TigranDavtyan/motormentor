import asyncio
import json
import logging
import random

import requests

from data_storage import db

logger = logging.getLogger()

with open('myautoge_ids.json', 'r') as file:
    myautoge_ids = json.load(file) 
    
for key, val in list(myautoge_ids.items()):
    for intkey, val in list(myautoge_ids[key].items()):
        myautoge_ids[key][int(intkey)] = val
        myautoge_ids[key].pop(intkey)

for brand_id in myautoge_ids['brand_ids'].keys():
    for key, val in list(myautoge_ids['brand_ids'][brand_id]['models'].items()):
        myautoge_ids['brand_ids'][brand_id]['models'][int(key)] = val
        myautoge_ids['brand_ids'][brand_id]['models'].pop(key)

def filter_and_transform_datapoint(d: dict) -> dict:
    return  {
        'itemid' :               d['car_id'],
        'website' :              'myauto.ge',
        'car_brand' :            myautoge_ids['brand_ids'][d['man_id']]['name'],
        'model' :                myautoge_ids['brand_ids'][d['man_id']]['models'][d['model_id']],
        'body_type' :            myautoge_ids['body_type_ids'][d['category_id']],
        'year' :                 d['prod_year'],
        'engine_type' :          myautoge_ids['engine_type_ids'][d['fuel_type_id']],
        'engine_size' :          d['engine_volume']/1000,
        'transmission' :         myautoge_ids['transmission_ids'][d['gear_type_id']],
        'drive_type' :           myautoge_ids['drive_type_ids'][d['drive_type_id']],
        'mileage' :              d['car_run_km'],
        # 'condition' :            d['car_id'],
        'gas_equipment' :        'installed' if d['fuel_type_id'] in [8,9] else 'no',
        'steering_wheel' :       myautoge_ids['wheel_type_ids'][d['right_wheel'] is True],
        'exterior_color' :       myautoge_ids['color_ids'][d['color_id']],
        'interior_color' :       myautoge_ids['interior_color_ids'][d['saloon_color_id']],
        'interior_material' :    myautoge_ids['interior_material_ids'][d['saloon_material_id']],
        'dollar_price' :         d['price_usd'],
        'original_price' :       d['price'],
        'posted_date' :          d['order_date'],
        'update_date' :          d['order_date'],
        'closed_item' :          0
    }

class MyAutoGe:
    def __init__(self):
        self.updated = 0
        self.same = 0
        self.error = 0
        self.no_price = 0
        self.closed = 0
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}
        self.url = 'https://api2.myauto.ge/en/products?TypeID=0&ForRent=0&Mans=&CurrencyID=1&MileageType=1&Customs=1&SortOrder=1&Page={page}'

        self.id_appender = 200000000000

    async def sleepRandom(self):
        await asyncio.sleep(random.random()*0.8 + 1)

    def getItemProperties(self, itemid):
        properties = db.fetchone('''SELECT car_brand,model,year,engine_size,engine_type,mileage,body_type,transmission,
        drive_type,gas_equipment,steering_wheel,exterior_color,interior_color,interior_material, dollar_price FROM listings WHERE itemid = ?''', (self.id_appender + int(itemid),)) 
        if not properties:
            return None
        car = {
            'car_brand' : properties[0],
            'model' : properties[1],
            'year' : properties[2],
            'engine_size' : properties[3],
            'engine_type' : properties[4],
            'mileage' : properties[5],
            'body_type' : properties[6],
            'transmission' : properties[7],
            'drive_type' : properties[8],
            'gas_equipment' : properties[9],
            'steering_wheel' : properties[10],
            'exterior_color' : properties[11],
            'interior_color' : properties[12],
            'interior_material' : properties[13],
            'dollar_price' : properties[14]
        }
        return car

    def getPage(self, page):
        res = requests.get(self.url.format(page=page), headers=self.headers)
        if res.status_code != 200:
            logger.error(f'Error for page {page}')
            self.error += 1
            return res.status_code, None, None
        
        page_content = json.loads(res.content.decode('utf-8'))

        npages = page_content['data']['meta']['last_page']
        nitems = page_content['data']['meta']['total']
        items = page_content['data']['items']

        return npages, nitems, items

    async def updateData(self, page_limit = None):
        db.createBackup()
        try:
            logger.info("STARTING TO SCRAPE MYAUTO GE")
            npages, nitems, _ = self.getPage(1)
            if page_limit and page_limit < npages:
                nitems = 15*page_limit
                npages = page_limit
            else:
                page_limit = 100000000000
            
            if nitems is None or self.error > 10:
                logger.error(f'Cant update data, last request status code is {npages}')
                return

            logger.info(f'Pages = {npages}  |  Total number of items = {nitems}')
            existing_ids = set([d[0] for d in db.fetchall('SELECT itemid FROM listings WHERE website = "myautoge" AND closed_item=0;')])
            same_or_updated = set()

            last_percent = 0
            for page in range(1, npages+1)[:page_limit]:
                npages, nitems, page_data = self.getPage(page)

                if self.error > 20 and self.error/(self.updated+self.same+self.no_price+1)*100 > 8:
                    logger.error(f'Cant update data, last request status code is {npages}')
                    db.restoreBackup()
                    return
                
                if not nitems :
                    self.error += 15
                    continue
                
                percent = round(page/npages*100)
                if percent != last_percent:
                    logger.info(f'Processed {percent}% of {nitems} items. Same {self.same} |  Updated {self.updated} |  Error {self.error} | No price {self.no_price} | Closed {self.closed}')
                    last_percent = percent

                for item in page_data:
                    item['car_id'] = self.id_appender + item['car_id']
                    if item['price_usd'] == 0:
                        self.no_price += 1
                        continue
                    try:
                        item_filtered = filter_and_transform_datapoint(item)
                        ret = db.insertOrUpdateListing(item_filtered)
                        if ret == 0:
                            self.same += 1
                        elif ret == 1:
                            self.updated += 1
                        same_or_updated.add(item['car_id'])

                    except Exception as e:
                        logger.error(f'Error for item {item["car_id"]}  '+str(e))
                        continue

                await self.sleepRandom()

            closed_ids = existing_ids.difference(same_or_updated)
            for id in closed_ids:
                db.closeItem(id)
        except Exception as e:
            logger.error('Stopping scraping because too many error '+str(e))
            db.restoreBackup()
        logger.info(f'Processed {nitems} items. Same {self.same} |  Updated {self.updated} |  Error {self.error} | No price {self.no_price} | Closed {self.closed}')
        logger.info("FINISHED SCRAPING MYAUTO GE")
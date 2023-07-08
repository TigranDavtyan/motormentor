import asyncio
import logging
import random
import re
import traceback
from datetime import datetime

import requests

from data_storage import db
from properties import *

logger = logging.getLogger('listamscraper')

class Parser:
    class Category:
        id_dollar = re.compile(r'item\/(\d+)\"><img data-original=\"//s\.list\.am/g/\d+/\d+\.[jpgwebp]+\"><div class=\"p\">(\$?[\d,]+ ?[֏₽]?)')#re.compile(r'item\/(\d+)\".+?<div class=\"p\">(\$?[\d,]+ ?[֏₽]?)')
        next_page = re.compile(r'</span> &nbsp; <a href="/category/\d+/(\d+)?.*">Next')

        def getItemIdPrices(page: str):
            return [[int(id), price.replace(',','').replace(' ','')] for id,price in Parser.Category.id_dollar.findall(page)]
        
        def getNextPageId(page: str):
            match = Parser.Category.next_page.search(page)
            if match:
                return match.group(1)
            return match
            
    class Item:
        dollar_price = re.compile(r'<span>\$(\d{1,3}(,\d{3})*(\.\d+)?)')
        dram_price = re.compile(r'<span>([\d,]+)\s*֏')
        ruble_price = re.compile(r'<span>([\d,]+)\s*₽')

        car_props = re.compile(r'<div class="c">(?:<div class="t">(?P<key>.*?)<\/div>)?<div class="i">(?P<value>.*?)<\/div><\/div>')

        car_brand = re.compile(r'bid=[0-9]+" itemprop="item"><span itemprop="name">(.*?)<\/span>')

        posted_dt = re.compile(r'Posted (\d{2}\.\d{2}\.\d{4})')
        renewed_dt = re.compile(r'Renewed (\d{2}\.\d{2}\.\d{4})')

        address = re.compile(r'title="Show the map" onclick="dlgo\(\'(.+?)\',\s*\'\/\?w=11&i=\d+&m=\d+\'')
        address2 = re.compile(r"onclick=\"dlgo\('(.+),\s*([\w\s]+)'\s*,\s*'/\?w=.*'\s*,\s*\d+\);return false;\">(.+)</a>")

        user = re.compile(r'<a href="/user/(\d+)" class')

        def getUser(page: str):
            userid = Parser.Item.user.search(page)
            if userid:
                userid = userid.group(1)
            return userid
        
        def getPrices(page: str):
            dollar_price,dram_price,ruble_price = None,None,None
            dollar_price = Parser.Item.dollar_price.search(page)
            if dollar_price: dollar_price = dollar_price.group(1)
            dram_price   = Parser.Item.dram_price.search(page)
            if dram_price: dram_price = dram_price.group(1)
            ruble_price  = Parser.Item.ruble_price.search(page)
            if ruble_price: ruble_price = ruble_price.group(1)
            
            return [dollar_price, dram_price, ruble_price]
        
        def getDatetimes(page: str):
            posted_match = Parser.Item.posted_dt.search(page)
            posted_date = None
            if posted_match:
                posted_date = posted_match.group(1)
                posted_date = datetime.strptime(posted_date, '%d.%m.%Y').date()

            return posted_date
        
        def getAddress(page: str):
            match = Parser.Item.address.search(page)
            address = match.group(1)

            city, street= None, None

            if address.find(',') > -1:
                street, city = address.split(',')
            elif address.find('›') > -1:
                city = address.split('›')[1].replace(' ','')
                
            return [city, street]

        def getCarBrand(page: str):
            brand_match = Parser.Item.car_brand.search(page)
            if brand_match:
                return brand_match.group(1)
            else:
                return None
            
        def getCar(page: str):
            # Extract item properties as dictionary
            properties = dict(Parser.Item.car_props.findall(page, re.DOTALL | re.IGNORECASE))
            properties = {k.lower().replace(' ', '_'): v.lower().replace(' ', '_') for k, v in properties.items() if v}
            properties['exterior_color'] = properties['color']
            properties.pop('color')

            if 'gas_equipment' not in properties.keys():
                properties['gas_equipment'] = 'no'

            if 'interior_color' not in properties.keys():
                properties['interior_color'] = 'black'

            try:
                car_brand = Parser.Item.getCarBrand(page)
                properties['car_brand'] = car_brand
            except:
                pass

            try:
                userid = Parser.Item.getUser(page)
                properties['userid'] = userid
            except:
                pass

            try:
                prices = Parser.Item.getPrices(page)
                properties['dollar_price'] = prices[0]
                properties['dram_price'] = prices[1]
                properties['ruble_price'] = prices[2]
            except:
                pass

            try:
                properties['posted_date'] = Parser.Item.getDatetimes(page)
            except:
                pass

            properties['update_date'] = datetime.now().date()
            properties['closed_item'] = 0
            
            for key, value in properties.items():
                properties[key] = CarProperties.get(key,value)
            
            if properties['car_brand'] == 'Kia' and properties['model'] == "cee'd":
                properties['model'] = 'ceed'

            if 'engine_size' not in properties.keys():
                engine_size = db.fetchone('''SELECT ROUND(AVG(engine_size), 1) FROM listings WHERE 
                car_brand = ? 
                AND model = ? 
                AND body_type = ? 
                AND year BETWEEN ? AND ?
                AND transmission = ?''',(properties['car_brand'], properties['model'],
                                          properties['body_type'], properties['year']-2,properties['year']+2, properties['transmission']))
                if engine_size:
                    properties['engine_size'] = engine_size[0]
                    logging.info(f'FOUND median engine size {engine_size[0]} for item {properties["car_brand"]} {properties["model"]} {properties["year"]}')
                else:
                    logging.info(f'NOT FOUND median engine size for item {properties["car_brand"]} {properties["model"]} {properties["year"]}')

            return properties
        

class ListAm:
    def __init__(self):
        self.item_url = 'https://www.list.am/en/item/{itemid}'
        self.url = 'https://www.list.am/en/category/23?type=1&n=0&bid=0&_a17=1'
        self.url_for_page = 'https://www.list.am/en/category/23/{page}?type=1&n=0&bid=0&_a17=1'
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}
        self.itemids = []

        self.updated = 0
        self.same = 0
        self.error = 0
        self.no_price = 0
        self.closed = 0

        self.id_appender = 100000000000

    async def sleepRandom(self):
        await asyncio.sleep(random.random()*0.8 + 0.5)

    def getUrl(self, page):
        if page > 1:
            page_url = self.url_for_page.format(page = page)
        else:
            page_url = self.url

        logger.debug(page_url)
        response = requests.get(page_url, headers=self.headers)
        if response.status_code != 200:
            logger.error(f'Response code {response.status_code}')
            return response.status_code
        return response.content.decode('utf-8')
       
    def getItem(self, itemid):
        url = self.item_url.format(itemid = itemid)
        logger.debug(url)
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            logger.error(f'Response code for {response.status_code} for {url}')
            return response.status_code
        return response.content.decode('utf-8')
    
    def getItemProperties(self, item):
        if type(item) == int:
            item_id = item
        elif type(item) == str:
            item_id = int(re.search(r"/(\d+)$", item).group(1))

        item_page = self.getItem(item_id)
        if type(item_page) == int:
            return None
        return Parser.Item.getCar(item_page)
    
    async def getItemIds(self, limit=None):
        next = 1
        global_limit = len(self.itemids) + limit if limit else 0
        while True:
            page = self.getUrl(next)
            if not page:
                continue
            
            idprices = Parser.Category.getItemIdPrices(page)
            for idprice in idprices:
                item = {}
                item['original_price'] = 0
                #$֏₽
                if '$' in idprice[1]:
                    item['dollar_price'] = int(idprice[1].replace('$',''))
                    item['original_price'] = item['dollar_price']
                elif '֏' in idprice[1]:
                    item['dram_price'] = int(idprice[1].replace('֏',''))
                    item['original_price'] = item['dram_price']
                elif '₽' in idprice[1]:
                    item['ruble_price'] = int(idprice[1].replace('₽',''))
                    item['original_price'] = item['ruble_price']

                item['itemid'] = idprice[0]
                self.itemids.append(item)

            if limit and len(self.itemids) > global_limit:
                self.itemids = self.itemids[:global_limit]
                break

            next = Parser.Category.getNextPageId(page)

            if not next:
                break
            next = int(next)
            
            await self.sleepRandom()

        self.itemids = list({item['itemid']:item for item in self.itemids}.values())


    async def getItems(self):
        db.createBackup()
        #if there is an item id which exists in db but not in the newly scraped list we flag them as finished
        existing_ids = set([d[0] for d in db.fetchall('SELECT itemid FROM listings WHERE website = "listam" AND closed_item=0;')])
        new_ids = set([self.id_appender + item['itemid'] for item in self.itemids])
        
        for itemid in existing_ids.difference(new_ids):
            db.closeItem(itemid)
            self.closed += 1
        del new_ids
        del existing_ids
        ###

        percent_modulo = int(len(self.itemids)/100)
        percent_modulo = 1 if percent_modulo == 0 else percent_modulo
        
        for i,item in enumerate(self.itemids):
            if i % percent_modulo == 0:
                logger.info(f'Processed {round(i/len(self.itemids)*100)}% of {len(self.itemids)} items. Same {self.same} |  Updated {self.updated} |  Error {self.error} | No price {self.no_price} | Closed {self.closed}')
            
            if self.error > 20 and self.error/(self.updated+self.same+self.no_price+1)*100 > 8:
                logger.error('Stopping scraping because too many error')
                db.restoreBackup()
                return False

            if item['original_price'] == 0: #Passing items which dont have a price
                self.no_price += 1
                continue

            op = db.fetchone('SELECT original_price FROM listings WHERE itemid = ?;',(self.id_appender + item['itemid'],))
            if op and op[0] == item['original_price']: #Passing items which are the same
                self.same += 1
                continue
            
            try:
                page = self.getItem(item['itemid'])
                item['itemid'] = self.id_appender + item['itemid']
                if page:
                    properties = Parser.Item.getCar(page)
                    properties['website'] = 'listam'
                    properties.update(item)

                    db.insertOrUpdateListing(properties)
                    self.updated += 1
                elif page == 404:
                    db.closeItem(item['itemid'])
                    self.closed += 1
                else:
                    raise ValueError('status code '+str(page))
                
            except Exception as e:
                logger.debug(f'{item["itemid"]} passed  '+ str(e))
                await asyncio.sleep(1)

                self.error += 1
                continue

            logger.debug(properties)
            del properties

            await self.sleepRandom()

        logger.info(f'ListAm For Sale Cars : Same {self.same} |  Updated {self.updated} |  Error {self.error} | No price {self.no_price} | Closed {self.closed}')
        return True
    

    async def update_data(self, limit = None):
        logger.info("STARTING TO SCRAPE LIST AM")

        logger.info('Getting item ids...')

        await self.getItemIds(limit)

        logger.info(f'Found {len(self.itemids)} listings')
        
        logger.info('Getting items...')
        try:
            await self.getItems()
        except Exception as e:
            logger.error('Stopping scraping because too many error ' + str(e))
            db.restoreBackup()
        
        logger.info("FINISHED SCRAPING LIST AM")
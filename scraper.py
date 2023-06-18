import re
from datetime import datetime
from properties import *
import logging
import traceback

logger = logging.getLogger('listamscraper')

class ListAmParser:
    class Category:
        id_dollar = r'item\/(\d+)\".+?<div class=\"p\">(\$?[\d,]+ ?[֏₽]?)'#<\/div>
        next_page = r'</span> &nbsp; <a href="/category/\d+/(\d+)?.*">Next'

        def getItemIdPrices(page: str):
            return [[int(id), price.replace(',','').replace(' ','')] for id,price in re.findall(ListAmParser.Category.id_dollar, page)]
        
        def getNextPageId(page: str):
            match = re.search(ListAmParser.Category.next_page, page)
            if match:
                return match.group(1)
            return match
            
    class Item:
        dollar_price = r'<span>\$(\d{1,3}(,\d{3})*(\.\d+)?)'
        dram_price = r'<span>([\d,]+)\s*֏'
        ruble_price = r'<span>([\d,]+)\s*₽'

        house_props = r'<div class="c">(?:<div class="t">(?P<key>.*?)<\/div>)?<div class="i">(?P<value>.*?)<\/div><\/div>'

        car_brand = r'bid=[0-9]+" itemprop="item"><span itemprop="name">(.*?)<\/span>'

        posted_dt = r'Posted (\d{2}\.\d{2}\.\d{4})'
        renewed_dt = r'Renewed (\d{2}\.\d{2}\.\d{4})'

        address = r'title="Show the map" onclick="dlgo\(\'(.+?)\',\s*\'\/\?w=11&i=\d+&m=\d+\''
        address2 = r"onclick=\"dlgo\('(.+),\s*([\w\s]+)'\s*,\s*'/\?w=.*'\s*,\s*\d+\);return false;\">(.+)</a>"

        user = r'<a href="/user/(\d+)" class'

        def getUser(page: str):
            userid = re.search(ListAmParser.Item.user, page)
            if userid:
                userid = userid.group(1)
            return userid
        
        def getPrices(page: str):
            dollar_price,dram_price,ruble_price = None,None,None
            dollar_price = re.search(ListAmParser.Item.dollar_price, page)
            if dollar_price: dollar_price = dollar_price.group(1)
            dram_price   = re.search(ListAmParser.Item.dram_price, page)
            if dram_price: dram_price = dram_price.group(1)
            ruble_price  = re.search(ListAmParser.Item.ruble_price, page)
            if ruble_price: ruble_price = ruble_price.group(1)
            
            return [dollar_price, dram_price, ruble_price]
        
        def getDatetimes(page: str):
            posted_match = re.search(ListAmParser.Item.posted_dt, page)
            renewed_match = re.search(ListAmParser.Item.renewed_dt, page)
            posted_date, renewed_date = None, None
            if posted_match:
                posted_date = posted_match.group(1)
                posted_date = datetime.strptime(posted_date, '%d.%m.%Y').date()

            if renewed_match:
                renewed_date = renewed_match.group(1)
                renewed_date = datetime.strptime(renewed_date, '%d.%m.%Y').date()
            else: renewed_date = posted_date

            return [posted_date,renewed_date]
        
        def getAddress(page: str):
            match = re.search(ListAmParser.Item.address, page)
            address = match.group(1)

            city, street= None, None

            if address.find(',') > -1:
                street, city = address.split(',')
            elif address.find('›') > -1:
                city = address.split('›')[1].replace(' ','')
                
            return [city, street]

        def getCarBrand(page: str):
            brand_match = re.search(ListAmParser.Item.car_brand, page)
            if brand_match:
                return brand_match.group(1)
            else:
                return None
            
        def getCar(page: str):
            # Extract item properties as dictionary
            properties = dict(re.findall(ListAmParser.Item.house_props, page, re.DOTALL | re.IGNORECASE))
            properties = {k.lower().replace(' ', '_'): v.lower().replace(' ', '_') for k, v in properties.items() if v}

            try:
                car_brand = ListAmParser.Item.getCarBrand(page)
                properties['car_brand'] = car_brand
            except:
                pass

            try:
                userid = ListAmParser.Item.getUser(page)
                properties['userid'] = userid
            except:
                pass

            try:
                prices = ListAmParser.Item.getPrices(page)
                properties['dollar_price'] = prices[0]
                properties['dram_price'] = prices[1]
                properties['ruble_price'] = prices[2]
            except:
                pass

            try:
                dts = ListAmParser.Item.getDatetimes(page)
                properties['posted_date'] = dts[0]
                properties['update_date'] = dts[1]
            except:
                pass
            
            # try:
            #     city, street = ListAmParser.Item.getAddress(page)
            #     properties['city'] = city
            #     properties['street'] = street
            # except:
            #     pass

            properties['closed_item'] = 0
            
            for key, value in properties.items():
                properties[key] = CarProperties.get(key,value)

            
            return properties
        

import time
import random
import requests

class ListAm:
    main = 'https://www.list.am/en/'
    # headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}# Mozilla
    def sleepRandom():
        #time.sleep(random.randint(1,3))
        time.sleep(random.random()*0.4 + 0.6)
        pass

    def getPageHtml(response: requests.Response) -> str:
        if response.status_code != 200:
            logger.error(response.status_code)
            return None

        with open('page.html','wb') as pagefile:
            pagefile.write(response.content)

        return response.content.decode('utf-8')

    def getUrl(url):
        logger.debug(url)
        response = requests.get(url, headers=ListAm.headers)
        if response.status_code != 200:
            logger.error(f'Response code {response.status_code}')
            return response.status_code
        return ListAm.getPageHtml(response)
       
    def getItem(item_id):
        url = ListAm.main + 'item/' + str(item_id)
        logger.debug(url)
        response = requests.get(url, headers=ListAm.headers)
        if response.status_code != 200:
            logger.error(f'Response code for {response.status_code} for {url}')
            return response.status_code
        return ListAm.getPageHtml(response)
    
import pandas as pd
import os
import pickle

class Category:
    def __init__(self, id, url, verbose=True):
        self.id = id
        self.url = url
        self.df = None
        self.itemids = []
        self.items = {}
        self.verbose = verbose
    
    def load(self):
        if len(getattr(self,'df',[])) > 0:
            return
        
        parent_class = None
        for cls in globals().values():
            if isinstance(cls, type) and issubclass(cls, object):
                for name, obj in cls.__dict__.items():
                    if obj is self:
                        parent_class = cls
                        self.clsname, self.objname = cls.__name__, name
        
        directory = f"{self.clsname}/{self.objname}"

        filename = f'{directory}/listings.csv'
        if os.path.isfile(filename):
            self.df = pd.read_csv(filename, index_col=0)
        else:
            os.makedirs(directory, exist_ok=True)

            self.df = pd.DataFrame(columns=parent_class.properties.getColumnNames())
            self.df.set_index('itemid', inplace=True)
            self.df.to_csv(filename, index=False)

        filename = f'{self.clsname}/{self.objname}/updates.pickle'
        if os.path.isfile(filename):
            with open(filename, 'rb') as f:
                self.items = pickle.load(f)
        else:
            self.items = {}

    def getUrl(self, page = None):
        if not page or page < 2:
            pagestr = ''
        else: pagestr = page

        return self.url.format(id=self.id, page=pagestr)

    def getItemIds(self, limit=None):
        next = None
        global_limit = len(self.itemids) + limit if limit else 0
        while True:
            page = ListAm.getUrl(self.getUrl(next))
            if not page:
                continue
            
            idprices = ListAmParser.Category.getItemIdPrices(page)
            idpricesparsed = []
            for idprice in idprices:
                item = {}
                #$֏₽
                if '$' in idprice[1]:
                    item['dollar_price'] = int(idprice[1].replace('$',''))
                elif '֏' in idprice[1]:
                    item['dram_price'] = int(idprice[1].replace('֏',''))
                elif '₽' in idprice[1]:
                    item['ruble_price'] = int(idprice[1].replace('₽',''))
                
                item['itemid'] = idprice[0]

                idpricesparsed.append(item)

            self.itemids.extend(idpricesparsed)

            if limit and len(self.itemids) > global_limit:
                self.itemids = self.itemids[:global_limit]
                break

            next = ListAmParser.Category.getNextPageId(page)

            if not next:
                break
            next = int(next)
            
            ListAm.sleepRandom()

        self.itemids = list({item['itemid']:item for item in self.itemids}.values())

    def getItems(self):
        self.load()
        
        updated = 0
        same = 0
        error = 0
        no_price = 0
        closed = 0

        #if there is an item id which exists in db but not in the newly scraped list we flag them as finished
        for itemid in self.df.index:
            new_ids = [item['itemid'] for item in self.itemids]
            if itemid not in new_ids:
                if itemid not in self.items:
                    self.items[itemid] = []
                self.items[itemid].append([datetime.now(), -1])
                self.df.at[itemid, 'closed_item'] = 1
                self.df.at[itemid, 'update_date'] = datetime.now().date()
                closed += 1
        ###

        percent_modulo = int(len(self.itemids)/100)
        for i,item in enumerate(self.itemids):
            if i % percent_modulo == 0:
                logger.info(f'Processed {round(i/len(self.itemids)*100)}% of {len(self.itemids)} items. Same {same} |  Updated {updated} |  Error {error} | No price {no_price} | Closed {closed}')

            new_dollar = item.get('dollar_price', None)
            new_dram   = item.get('dram_price', None)
            new_ruble  = item.get('ruble_price', None)

            if not new_dollar and not new_dram and not new_ruble: #Passing items which dont have a price
                no_price += 1
                continue

            try:
                old_dollar = self.df.at[item['itemid'],'dollar_price']
                old_dram = self.df.at[item['itemid'],'dram_price']
                old_ruble = self.df.at[item['itemid'],'ruble_price']
                if old_dollar and new_dollar and old_dollar == new_dollar:
                    same += 1
                    continue
                elif old_dram and new_dram and old_dram == new_dram:
                    same += 1
                    continue
                elif old_ruble and new_ruble and old_ruble == new_ruble:
                    same += 1
                    continue
            except Exception as e:
                if type(e) == KeyError:
                    logger.debug(type(e).__name__+" – "+str(e))
                else:
                    logger.error(type(e).__name__+" – "+str(e))
                    
            try:
                page = ListAm.getItem(item['itemid'])
                if page:
                    properties = ListAmParser.Item.getCar(page)
                    properties.update(item)
                    updated += 1
                elif page == 404:
                    closed += 1
                    self.items[itemid].append([datetime.now(), -1])
                    self.df.at[itemid, 'closed_item'] = 1
                    self.df.at[itemid, 'update_date'] = datetime.now().date()

            except Exception as e:
                traceback.print_exc()
                logger.error(f'{item} passed because {e}')
                error+=1
                continue

            logger.debug(properties)

            self.df.loc[properties['itemid']] = properties

            if properties['itemid'] not in self.items.keys():
                self.items[properties['itemid']] = []

            date = properties['update_date']# if 'update_date' in properties.keys() and properties['update_date'] else properties['posted_date']
            self.items[properties['itemid']].append([date, properties['dollar_price']])

            ListAm.sleepRandom()

        logger.info(f'Category {self.clsname}/{self.objname}  Same {same} |  Updated {updated} |  Error {error} | No price {no_price} | Closed {closed}')

    def save(self):
        directory = f'{self.clsname}/{self.objname}'
        os.makedirs(directory, exist_ok=True)

        self.df.to_csv(f'{directory}/listings.csv')
        
        with open(f'{directory}/updates.pickle', 'wb') as f:
            pickle.dump(self.items, f)

    def clear(self):
        del self.itemids
        del self.items
        del self.df
        self.itemids = []
        self.items = {}
        self.df = None

class ForSale:
    url = 'https://www.list.am/en/category/{id}/{page}'

    properties = CarProperties

    Cars = Category(23, url)
import logging
import datetime
import sys
import time
import os
import platform

from scraper import ForSale

def log_exceptions(exctype, value, traceback):
    logger = logging.getLogger('listamscraper')
    logger.error(exctype, value, traceback)
    sys.__excepthook__(exctype, value, traceback)

sys.excepthook = log_exceptions

def botlog(log_message):
    logger = logging.getLogger('listamscraper')
    logger.info(log_message)

def run():
    logger = logging.getLogger('listamscraper')
    logger.setLevel(logging.INFO)

    # create file handler
    fh = logging.FileHandler('listamscraper.log','a', 'utf-8')

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(fh)

    botlog("START TO SCRAPE")

    logger.info('Getting item ids...')

    itemids_len = len(ForSale.Cars.itemids)
    ForSale.Cars.getItemIds(limit=100)
    itemids_len = len(ForSale.Cars.itemids) - itemids_len

    logger.info(f'Found {itemids_len} listings')

    logger.info('Getting items...')
    ForSale.Cars.getItems()

    logger.info('Saving data...')
    ForSale.Cars.save()
    
    botlog("FINISHED SCRAPING")
    

if __name__ == '__main__':
    if len(sys.argv) == 2:
        run_time = time.strptime(sys.argv[1], '%H:%M')
        now = datetime.datetime.now()
        next_run = now.replace(hour=run_time.tm_hour, minute=run_time.tm_min, second=0)
        if next_run < now:
            next_run += datetime.timedelta(days=1)
        wait_time = (next_run - now).total_seconds()-1
        print('Next run',next_run,'   wait time ', wait_time,'(seconds)')
    else:
        print('No time parameter. You should give a time parameter like this main.py 8:00')
        next_run = datetime.datetime.now()
        wait_time = 0

    if platform.system() in ['Linux', 'Darwin']:
        # Update the time zone information
        os.environ['TZ'] = 'Asia/Yerevan'
        time.tzset()

    while True:
        time.sleep(wait_time)

        run()

        now = datetime.datetime.now()
        next_run += datetime.timedelta(days=1)
        wait_time = (next_run - now).total_seconds()

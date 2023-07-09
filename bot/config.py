import os
import time
import platform

if platform.system() in ['Linux', 'Darwin']:
    print('Running production mode on MotorMentor')
    # Set the TZ environment variable
    os.environ['TZ'] = 'Asia/Yerevan'

    # Update the time zone information
    time.tzset()

    TOKEN = '5945899256:AAHkaeHkf9GZwKSNbV2HoDz1oXW3khjuTL0'

    BOT_USERNAME = 'motormentorbot'
    REPORT_CHANNEL_ID = -1001507986820
else:
    print('Development mode on davtyantestbot')
    TOKEN = os.environ.get('TEST_BOT_TOKEN')

    BOT_USERNAME = 'propertizebot'
    REPORT_CHANNEL_ID = -1001830553096

PROJECT_NAME = "MotorMentor"

DB_PATH = 'data/bot.db'

AMD2USD = 0
AMD2RUB = 0

# ADMIN_CHAT_ID = 1710831153 #Tigran Davtyan
ADMIN_CHAT_ID = 1859746511#Motor Mentor Admin

DEFAULT_LANGUAGE = 0 #Armenian

NIGHT_HOURS = {'start':23,'end': 10}

SUBSCRIPTION_DAYS = 30
BONUS_REFS = 5
BONUS_DAYS_FOR_REFS = SUBSCRIPTION_DAYS

LISTAM_ID_APPENDER   = 100000000000
MYAUTOGE_ID_APPENDER = 200000000000

class LOCATIONS:
    ARM = 0
    GE = 1
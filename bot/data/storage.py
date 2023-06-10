import sqlite3 as lite
import config
import logging

language_suffixes = ['phrase_arm','phrase_rus','phrase_eng']

def log_queries(query):
    #if query.startswith(("INSERT", "UPDATE", "DELETE", "insert", "update", "delete")):
    logging.debug('SQL: '+query)
    

class DatabaseManager(object):
    def __init__(self):
        self.conn = lite.connect(config.DB_PATH)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        
        self.conn.set_trace_callback(log_queries)

        self.cur = self.conn.cursor()
        self.create_tables()
        self.current_phrase_id = self.fetchone('SELECT MAX(id) FROM phrases')
        self.current_phrase_id = 999 if self.current_phrase_id[0] is None else self.current_phrase_id[0]

    def getNextPhraseId(self):
        self.current_phrase_id += 1
        return self.current_phrase_id

    def userExists(self, cid: int):
        return self.fetchone('SELECT count(cid) > 0 FROM users where cid=?;',(cid,))[0]

    def getUserLang(self, cid: int):
        return self.fetchone('SELECT preferred_language FROM users WHERE cid=?;',(cid,))[0]
    
    def setUserLang(self, cid: int, lang: int):
        self.query('UPDATE users SET preferred_language=? WHERE cid=?;',(lang,cid))

    def getUserName(self, cid):
        name = self.fetchone('SELECT name FROM users WHERE cid=?',(cid,))
        if name:
            return name[0]
        else:
            return 'Anon'
    
    def getUserSubscription(self, cid):
        return self.fetchone('SELECT subscription FROM users WHERE cid=?',(cid,))[0]
        
    def getPhraseForUser(self, id: int, cid: int):
        lang = self.getUserLang(cid)
        return self.fetchone(f'SELECT {language_suffixes[lang]} FROM phrases WHERE id=?;', (id,))[0]

    def getPhraseAll(self, id: int):
        return self.fetchone(f'SELECT phrase_arm, phrase_rus, phrase_eng FROM phrases WHERE id=?;', (id,))

    def addPhrase(self, phrase: str) -> int:
        id = self.getNextPhraseId()
        self.query('INSERT INTO phrases VALUES (?,?,?,?)',(id,phrase,phrase,phrase))
        return id

    def setPhrase(self, id :int, phrase: str):
        self.query('UPDATE phrases SET phrase_arm=?, phrase_rus=?, phrase_eng=? WHERE id=?',(phrase,phrase,phrase,id))

    def setPhraseForLang(self, id :int, phrase: str, lang: int):
        self.query(f'UPDATE phrases SET {language_suffixes[lang]}=? WHERE id=?',(phrase,id))

    def getState(self, cid: int):
        state_id = self.fetchone('SELECT state_id FROM users WHERE cid = ?;',(cid,))[0]
        return state_id

    def setState(self, cid: int, state_id : int):
        self.query('UPDATE users SET state_id = ? WHERE cid=?;',(state_id,cid))

    def create_tables(self):
        self.query('''CREATE TABLE IF NOT EXISTS users 
                   (cid INTEGER PRIMARY KEY, name TEXT, phone_number TEXT, joining_date DATETIME, account_state INTEGER,
                    state_id INTEGER, preferred_language INTEGER, subscription INTEGER DEFAULT 0, subscription_end DATETIME DEFAULT '2025-01-01 00:00:00',
                      next_payment_amount INTEGER DEFAULT 0)''')

        self.query('CREATE TABLE IF NOT EXISTS phrases (id INTEGER PRIMARY KEY, phrase_arm TEXT, phrase_rus TEXT, phrase_eng TEXT)')

        self.query('''CREATE TABLE IF NOT EXISTS car_prices (cid INTEGER PRIMARY KEY, car_brand TEXT, model TEXT,
        year INTEGER, mileage REAL, exterior_color TEXT, body_type TEXT, engine_type TEXT, engine_size REAL,transmission TEXT,
        drive_type TEXT,condition TEXT,gas_equipment TEXT,steering_wheel TEXT,headlights TEXT,interior_color TEXT,interior_material TEXT,
        sunroof TEXT, wheel_size REAL, price REAL)''')

        self.query('''CREATE TABLE IF NOT EXISTS user_cars (cid INTEGER PRIMARY KEY, car_brand TEXT, model TEXT,
        year INTEGER, mileage REAL, exterior_color TEXT, body_type TEXT, engine_type TEXT, engine_size REAL,transmission TEXT,
        drive_type TEXT,condition TEXT,gas_equipment TEXT,steering_wheel TEXT,headlights TEXT,interior_color TEXT,interior_material TEXT,
        sunroof TEXT, wheel_size REAL, price REAL)''')
        
        self.query('''CREATE TABLE IF NOT EXISTS car_price_results (cid INTEGER, car_brand TEXT, model TEXT,
        year INTEGER, mileage REAL, exterior_color TEXT, body_type TEXT, engine_type TEXT, engine_size REAL,transmission TEXT,
        drive_type TEXT,condition TEXT,gas_equipment TEXT,steering_wheel TEXT,headlights TEXT,interior_color TEXT,interior_material TEXT,
        sunroof TEXT, wheel_size REAL, price REAL)''')

        self.query('CREATE TABLE IF NOT EXISTS files (filename TEXT PRIMARY KEY, fileid INTEGER)')

        self.query('CREATE TABLE IF NOT EXISTS ads (id INTEGER PRIMARY KEY AUTOINCREMENT, active INTEGER DEFAULT 1, click_count INTEGER DEFAULT 0, price TEXT, language INTEGER, messageid INTEGER)')

    def query(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.conn.commit()

    def fetchone(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()

    def fetchall(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()
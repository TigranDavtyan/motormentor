import sqlite3 as lite
import ast
import datetime

class DataDatabase:
    def __init__(self, path):
        self.conn = lite.connect(path)
        self.cur = self.conn.cursor()

        self.createTables()

    def createTables(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS listings (itemid INTEGER PRIMARY KEY, website TEXT, car_brand TEXT, model TEXT,
                year INTEGER, mileage REAL, exterior_color TEXT, body_type TEXT, engine_type TEXT, engine_size REAL,transmission TEXT,
                drive_type TEXT, gas_equipment TEXT, steering_wheel TEXT, interior_color TEXT, interior_material TEXT,
                dollar_price REAL, original_price REAL,posted_date DATETIME, update_date DATETIME, closed_item INTEGER, updates TEXT DEFAULT '{}')''')
        
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

    def insertOrUpdateListing(self, item):
        '''same - 0  |  updated - 1'''

        item_db = self.fetchone('SELECT itemid, original_price, updates FROM listings WHERE itemid = ?;', (item['itemid'],))
        if item_db:
            if item_db[1] != item['original_price']:

                updates = ast.literal_eval(item_db[2])
                updates[str(item['update_date'])] = item['original_price']
                self.query("""UPDATE listings SET original_price = ?, dollar_price = ?, update_date = DATETIME('now'), updates = ?
                  WHERE itemid = ?""", (item['original_price'], item['dollar_price'], str(updates), item['itemid']))
                print('+++++++++  Updated ', item['itemid'])
                return 1
            else:
                db.query('UPDATE listings SET closed_item = 0 WHERE itemid = ?;',(item['itemid'],))
                return 0
        else:
            updates = {str(item['update_date']):item['original_price']}
            self.query("INSERT INTO listings VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (item['itemid'], item['website'], item['car_brand'],item['model'],item['year'],
                                                                                        item['mileage'],item['exterior_color'],item['body_type'],item['engine_type'],
                                                                                        item['engine_size'],item['transmission'],item['drive_type'],item['gas_equipment'],
                                                                                        item['steering_wheel'],item['interior_color'],item['interior_material'],item['dollar_price'],
                                                                                        item['original_price'],item['posted_date'],item['update_date'],item['closed_item'], str(updates)))
            return 0
        
    def closeItem(self, itemid):
        updates = ast.literal_eval(self.fetchone('SELECT updates FROM listings WHERE itemid = ?;', (itemid,))[0])

        updates[str(datetime.datetime.now().date())] = -1

        self.query("UPDATE listings SET closed_item = 1, update_date = DATETIME('now'), updates = ? WHERE itemid = ?", (str(updates), itemid))

db = DataDatabase('data.db')
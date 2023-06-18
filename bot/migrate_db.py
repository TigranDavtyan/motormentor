from data.storage import DatabaseManager
db = DatabaseManager()

# db.query('ALTER TABLE users ADD COLUMN account_state INTEGER DEFAULT 0')
db.query("ALTER TABLE users ADD COLUMN referral_id TEXT DEFAULT ''")
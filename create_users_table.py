import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "nidah.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    country TEXT,
    cadre TEXT,
    specialization TEXT,
    password TEXT NOT NULL,
    role TEXT NOT NULL,
    status TEXT DEFAULT 'active'
)
""")

conn.commit()
conn.close()
print("Users table created (or already exists).")

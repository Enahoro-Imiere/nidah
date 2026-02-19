import sqlite3
import os

# Path to your database
DB_PATH = os.path.join(os.path.dirname(__file__), "nidah.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create programs table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS programs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    active INTEGER DEFAULT 1
)
""")

# Optionally, insert some sample programs
cursor.execute("INSERT OR IGNORE INTO programs (id, name, description, active) VALUES (1, 'Maternal & Child Health', 'MCH capacity strengthening initiatives', 1)")
cursor.execute("INSERT OR IGNORE INTO programs (id, name, description, active) VALUES (2, 'Oncology', 'Cancer care collaboration and specialist exchange', 1)")
cursor.execute("INSERT OR IGNORE INTO programs (id, name, description, active) VALUES (3, 'Ophthalmology', 'Eye care services and specialist training', 1)")
cursor.execute("INSERT OR IGNORE INTO programs (id, name, description, active) VALUES (4, 'Urology', 'Advanced urological care and training', 1)")
cursor.execute("INSERT OR IGNORE INTO programs (id, name, description, active) VALUES (5, 'Neurology', 'Specialist neurological services and capacity building', 1)")

conn.commit()
conn.close()
print("Programs table created (or already exists) and sample programs added.")

import sqlite3
import os

# Path to your database
DB_PATH = os.path.join(os.path.dirname(__file__), "nidah.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create interests table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS interests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    period TEXT DEFAULT '',
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(program_id) REFERENCES programs(id)
)
""")

conn.commit()
conn.close()
print("Interests table created or already exists.")

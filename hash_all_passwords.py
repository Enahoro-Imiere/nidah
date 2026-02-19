import psycopg2
import bcrypt
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "host": "localhost",
    "dbname": "nidah_db",
    "user": "nidah_admin",
    "password": "12345"
}

def hash_facilities():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("ALTER TABLE facilities ADD COLUMN IF NOT EXISTS password_hash TEXT")
    cur.execute("SELECT id, password FROM facilities")
    facilities = cur.fetchall()
    for f in facilities:
        if f['password']:
            hashed = bcrypt.hashpw(f['password'].encode(), bcrypt.gensalt()).decode()
            cur.execute("UPDATE facilities SET password_hash=%s WHERE id=%s", (hashed, f['id']))
    conn.commit()
    cur.close()
    conn.close()
    print("Facility passwords hashed!")

def hash_admins():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("ALTER TABLE admin_accounts ADD COLUMN IF NOT EXISTS password_hash TEXT")
    cur.execute("SELECT id, password FROM admin_accounts")
    admins = cur.fetchall()
    for a in admins:
        if a['password']:
            hashed = bcrypt.hashpw(a['password'].encode(), bcrypt.gensalt()).decode()
            cur.execute("UPDATE admin_accounts SET password_hash=%s WHERE id=%s", (hashed, a['id']))
    conn.commit()
    cur.close()
    conn.close()
    print("Admin passwords hashed!")

if __name__ == "__main__":
    hash_facilities()
    hash_admins()
    print("All passwords are now hashed!")

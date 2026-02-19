import psycopg2
import bcrypt

# --- Connect to PostgreSQL ---
conn = psycopg2.connect(
    host="localhost",
    dbname="nidah_db",
    user="nidah_admin",
    password="12345"
)
cur = conn.cursor()

# --- Default password ---
default_pw = "nid123"
hashed_pw = bcrypt.hashpw(default_pw.encode(), bcrypt.gensalt()).decode()

# --- Update only facilities without a password ---
cur.execute("""
    UPDATE facilities
    SET password_hash = %s
    WHERE password_hash IS NULL
""", (hashed_pw,))

conn.commit()
cur.close()
conn.close()

print("Default password applied to all facilities without one.")

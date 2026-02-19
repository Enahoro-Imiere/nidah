from database.db import get_connection
from auth.auth_utils import hash_password

def seed_dummy_data():
    conn = get_connection()
    cursor = conn.cursor()

    # ---- USERS ----
    users = [
        ("admin", hash_password("admin123"), "admin"),
        ("john_doe", hash_password("password123"), "individual"),
        ("nma_rep", hash_password("password123"), "association"),
        ("lagos_hospital", hash_password("password123"), "facility"),
    ]

    for u in users:
        try:
            cursor.execute(
                "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                u
            )
        except:
            pass  # ignore duplicates

    # ---- PROGRAMS ----
    programs = [
        ("Neurology", "Specialist neurological services and capacity building"),
        ("Urology", "Advanced urological care and training"),
        ("Ophthalmology", "Eye care services and specialist training"),
        ("Oncology", "Cancer care collaboration and specialist exchange"),
        ("Maternal & Child Health", "MCH capacity strengthening initiatives"),
    ]

    for p in programs:
        try:
            cursor.execute(
                "INSERT INTO programs (name, description) VALUES (?, ?)",
                p
            )
        except:
            pass

    # ---- FACILITY SERVICES ----
    cursor.execute("""
        INSERT OR IGNORE INTO facilities (user_id, facility_name, services, status)
        SELECT id, 'Lagos University Teaching Hospital',
               'Neurology, Oncology, Radiology, Emergency Care',
               'approved'
        FROM users WHERE username='lagos_hospital'
    """)

    # ---- USER INTERESTS ----
    cursor.execute("""
        INSERT OR IGNORE INTO interests (user_id, program_id)
        SELECT u.id, p.id
        FROM users u, programs p
        WHERE u.username='john_doe' AND p.name='Neurology'
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO interests (user_id, program_id)
        SELECT u.id, p.id
        FROM users u, programs p
        WHERE u.username='nma_rep' AND p.name='Ophthalmology'
    """)

    conn.commit()
    conn.close()
    print("✅ Dummy data seeded successfully.")

if __name__ == "__main__":
    seed_dummy_data()

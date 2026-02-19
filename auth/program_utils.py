from database.db import get_connection

def create_program(name, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO programs (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()

def get_programs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description FROM programs")
    programs = cursor.fetchall()
    conn.close()
    return programs

def indicate_interest(user_id, program_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO interests (user_id, program_id) VALUES (?, ?)", (user_id, program_id))
    conn.commit()
    conn.close()

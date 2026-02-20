import psycopg2
import bcrypt
import uuid
from psycopg2.extras import RealDictCursor

from database.connection import get_connection

def authenticate_facility(facility_code, password):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""
        SELECT id, facility_name, facility_code, password_hash
        FROM facilities
        WHERE facility_code = %s
    """, (facility_code,))

    facility = cur.fetchone()
    cur.close()
    conn.close()

    if not facility:
        return None

    if not facility["password_hash"]:
        return None

    valid = bcrypt.checkpw(
        password.encode(),
        facility["password_hash"].encode()
    )

    if valid:
        return facility

    return None


# utils.py

def generate_verification_token():
    return str(uuid.uuid4())

def send_verification_email(user_email, token):
    verification_link = f"https://yourportal.com/verify_email?token={token}"
    subject = "Verify Your NiDAH-P Account"
    body = f"Hi! Please verify your email by clicking the link below:\n{verification_link}"
    
    # Replace this with your actual email sending logic
    send_email(to=user_email, subject=subject, body=body)


def send_email(to, subject, body):
    import smtplib
    from email.mime.text import MIMEText

    sender_email = "yourgmail@gmail.com"
    sender_app_password = "your_app_password_here"  # 16-char app password

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_app_password)
        server.sendmail(sender_email, to, msg.as_string())

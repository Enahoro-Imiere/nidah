# utils.py
import uuid

def generate_verification_token():
    return str(uuid.uuid4())

def send_verification_email(user_email, token):
    verification_link = f"https://yourportal.com/?page=verify_email&token={token}"
    subject = "Verify Your NiDAH-P Account"
    body = f"Hi! Please verify your email by clicking the link below:\n{verification_link}"

    # Replace this with your actual email sending logic
    send_email(to=user_email, subject=subject, body=body)

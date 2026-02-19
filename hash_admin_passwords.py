import bcrypt

password = "admin123"  # desired admin password
hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
print(hashed.decode())  # copy this value

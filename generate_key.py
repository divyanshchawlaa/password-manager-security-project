from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("keys/secret.key", "wb") as f:
    f.write(key)

print("Key generated successfully")
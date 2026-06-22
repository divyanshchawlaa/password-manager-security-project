from cryptography.fernet import Fernet

with open("keys/secret.key", "rb") as f:
    key = f.read()

cipher = Fernet(key)


def encrypt_password(password):

    return cipher.encrypt(
        password.encode()
    ).decode()


def decrypt_password(encrypted_password):

    return cipher.decrypt(
        encrypted_password.encode()
    ).decode()
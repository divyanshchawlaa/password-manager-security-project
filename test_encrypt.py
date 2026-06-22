from encryption import (
    encrypt_password,
    decrypt_password
)

password = "MyPassword123"

encrypted = encrypt_password(password)

print(encrypted)

print(
    decrypt_password(encrypted)
)
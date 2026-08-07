from cryptography.fernet import Fernet

# Load the key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Read contacts.json
with open("contacts.json", "rb") as file:
    data = file.read()

# Encrypt
encrypted = cipher.encrypt(data)

# Save encrypted file
with open("contacts.enc", "wb") as file:
    file.write(encrypted)

print("Contacts encrypted successfully.")

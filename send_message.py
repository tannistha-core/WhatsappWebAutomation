"""
PROJECT STRUCTURE : Whatsapp Automation
contacts.json
send_message.py
message.txt

"""
import json
import time
import pywhatkit
from cryptography.fernet import Fernet

# Read encryption key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Read encrypted contacts
with open("contacts.enc", "rb") as file:
    encrypted_data = file.read()

# Decrypt contacts
contacts = json.loads(cipher.decrypt(encrypted_data))

# Read message template
with open("message.txt", "r", encoding="utf-8") as file:
    template = file.read()

print("Starting WhatsApp Automation...\n")

for person in contacts["contacts"]:

    message = template.format(
        name=person["name"]
    )

    print(f"Sending message to {person['name']}")

    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=person["phone"],
            message=message,
            wait_time=15,
            tab_close=True,
            close_time=5
        )

        print("✓ Message Sent\n")

    except Exception as e:
        print("✗ Failed")
        print(e)

    # Wait before sending next message
    time.sleep(20)

print("All messages processed.")

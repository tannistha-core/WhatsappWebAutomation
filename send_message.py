"""
PROJECT STRUCTURE : Whatsapp Automation
contacts.json
send_message.py
message.txt

"""
import json
import pywhatkit
import time

## Read contacts
with open("contacts.json", "r") as file:
    data = json.load(file)

## Read Message
with open("message.txt", "r") as file:
    message = file.read()

print("Sending messages.... \n")

for contact in data["contacts"]:
    print(f"Sending to {contact['name']}")

    pywhatkit.sendwhatmsg_instantly(
        phone_no = contact["phone"],
        message = message,
        wait_time = 15,
        tab_close = True,
        close_time = 5
    )

    # wait before sending the next message
    time.sleep(20)

print("\nAll messages sent successfully")
    

# Whatsapp Web Automation
#📱 WhatsApp Automation with Encrypted Contacts

A secure Python-based automation tool designed to send personalized WhatsApp messages using `pywhatkit`, featuring local contact encryption via `cryptography` to keep sensitive phone numbers safe.

---

## 🔒 Security Overview

To protect user privacy, raw contact details are never stored in plain text. Contacts are encrypted using Fernet symmetric encryption (AES-128 in CBC mode) before being saved locally.

> ⚠️ **Important:** Never upload `secret.key`, `contacts.json`, or `contacts.enc` to public repositories.

---

## 🛠️ Project Structure

```text
├── generate_key.py      # Generates a secret Fernet encryption key
├── encrypt_contacts.py  # Encrypts local contacts.json into contacts.enc
├── send_message.py      # Main script to decrypt contacts and send WhatsApp messages
├── message.txt          # Customizable message template
├── requirements.txt     # Required Python libraries
└── README.md            # Project documentation

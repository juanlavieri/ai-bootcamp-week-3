import csv
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

# Uncomment the following lines to generate the key when needed.
# WARNING: Run this only once, or you will not be able to decrypt previously encrypted data.
# generate_key()
# print("A new 'secret.key' has been generated and saved. Keep this file secure!")


def load_key():
    return open('secret.key', 'rb').read()

def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message.encode()).decode()

def load_accounts(key):
    accounts = {}
    try:
        with open('./data/accounts.csv', mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header
            for row in csv_reader:
                account_number, encrypted_pin, balance = row
                accounts[account_number] = {
                    'pin': decrypt_message(encrypted_pin, key),
                    'balance': float(balance)
                }
    except FileNotFoundError:
        pass
    return accounts

def save_accounts(accounts, key):
    with open('./data/accounts.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["account_number", "pin", "balance"])  # Write header
        for account_number, account_data in accounts.items():
            encrypted_pin = encrypt_message(account_data['pin'], key)
            csv_writer.writerow([account_number, encrypted_pin, account_data['balance']])

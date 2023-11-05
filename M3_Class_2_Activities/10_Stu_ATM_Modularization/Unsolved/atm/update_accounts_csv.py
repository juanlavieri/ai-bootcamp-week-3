from utils import encrypt_message, load_key
import csv
import random

# Load the encryption key
key = load_key()

# Function to generate a unique 10-digit account number
def generate_account_number(existing_numbers):
    while True:
        account_number = str(random.randint(1000000000, 9999999999))
        if account_number not in existing_numbers:
            return account_number

# Read the original accounts data
original_data_path = './data/original_accounts.csv'
updated_data_path = './data/accounts.csv'

existing_numbers = set()
updated_accounts_data = []

with open(original_data_path, mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header
    for row in csv_reader:
        pin, balance = row
        account_number = generate_account_number(existing_numbers)
        existing_numbers.add(account_number)
        encrypted_pin = encrypt_message(pin, key)
        updated_accounts_data.append((account_number, encrypted_pin, balance))

# Write the updated data to accounts.csv
with open(updated_data_path, mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["account_number", "pin", "balance"])  # Write header
    for account in updated_accounts_data:
        csv_writer.writerow(account)

print("accounts.csv has been updated with encrypted PINs and assigned account numbers.")

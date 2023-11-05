import unittest
from unittest.mock import patch
from cryptography.fernet import Fernet
from modular_atm import ATM

# Util function to load encryption key
def load_key():
    with open('secret.key', 'rb') as file:
        return file.read()

# Util function to encrypt a message
def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

# Util function to decrypt a message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message.encode()).decode()

# ATM class tests
class TestATM(unittest.TestCase):
    def setUp(self):
        self.key = load_key()
        self.atm = ATM(self.key)
        self.account_number = '9831350653'
        self.pin = '1227'
        self.encrypted_pin = encrypt_message(self.pin, self.key)
        self.atm.accounts[self.account_number] = {'pin': self.encrypted_pin, 'balance': 100.0}

    def test_deposit(self):
        # Assuming the deposit method takes the account number and the amount
        self.atm.deposit(self.account_number, 50)
        self.assertEqual(self.atm.accounts[self.account_number]['balance'], 150.0)

    def test_withdraw(self):
        # Assuming the withdraw method takes the account number and the amount
        self.atm.withdraw(self.account_number, 50)
        self.assertEqual(self.atm.accounts[self.account_number]['balance'], 50.0)

    def test_check_balance(self):
        # Assuming the check_balance method returns the balance
        balance = self.atm.check_balance(self.account_number)
        self.assertEqual(balance, 100.0)

    def test_change_pin(self):
        # Assuming the change_pin method takes the account number, old PIN, and new PIN
        self.atm.change_pin(self.account_number, self.pin, '3344')
        new_encrypted_pin = self.atm.accounts[self.account_number]['pin']
        self.assertEqual(decrypt_message(new_encrypted_pin, self.key), '3344')

    def test_invalid_transaction(self):
        # Assuming an invalid transaction returns False or raises an error
        with self.assertRaises(ValueError):
            self.atm.execute_transaction(self.account_number, 'invalid_transaction_type')

    # Add other necessary tests depending on the implementation details of your ATM class

if __name__ == '__main__':
    unittest.main()

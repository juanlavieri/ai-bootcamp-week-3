import random
from utils import load_key, encrypt_message, decrypt_message, load_accounts, save_accounts

# Define a class to represent the Bank Account
class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited. New balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} has been withdrawn. New balance is {self.balance}.")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(f"The current balance is {self.balance}.")

    def change_pin(self, old_pin, new_pin, key):
        if decrypt_message(self.pin, key) == old_pin:
            self.pin = encrypt_message(new_pin, key)
            print("PIN changed successfully.")
        else:
            print("Incorrect old PIN.")

# Define a class to represent the ATM
class ATM:
    def __init__(self, key):
        self.key = key
        self.accounts = load_accounts(key)

    def generate_account_number(self):
        while True:
            account_number = str(random.randint(1000000000, 9999999999))
            if account_number not in self.accounts:
                return account_number

    def create_account(self):
        account_number = self.generate_account_number()
        print(f"Your new account number is {account_number}. Please save this number.")

        pin = input("Choose your PIN (4 digits): ")
        while not (pin.isdigit() and len(pin) == 4):
            print("Invalid PIN format. The PIN must be 4 digits.")
            pin = input("Choose your PIN (4 digits): ")

        confirm_pin = input("Confirm your PIN: ")
        while pin != confirm_pin:
            print("PINs do not match. Please try again.")
            pin = input("Choose your PIN (4 digits): ")
            confirm_pin = input("Confirm your PIN: ")

        encrypted_pin = encrypt_message(pin, self.key)
        self.accounts[account_number] = {'pin': encrypted_pin, 'balance': 0}
        save_accounts(self.accounts, self.key)
        print("Account created successfully. Please remember your PIN and account number.")

    def verify_account(self, account_number, pin):
        if account_number in self.accounts and decrypt_message(self.accounts[account_number]['pin'], self.key) == pin:
            print("PIN verified successfully.")
            return True
        else:
            print("Incorrect account number or PIN.")
            return False

    def attempt_login(self):
        for _ in range(3):
            user_account_number = input("Please enter your account number: ")
            user_pin = input("Please enter your PIN: ")
            if self.verify_account(user_account_number, user_pin):
                return user_account_number
            else:
                print("Authentication failed. Please try again.")
        print("Too many failed attempts. Returning to the main menu.")
        return None

    def execute_transaction(self, account_number):
        account_data = self.accounts[account_number]
        account = BankAccount(account_number, account_data['pin'], account_data['balance'])
        while True:
            choice = self.select_transaction()
            if choice == "1":
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif choice == "3":
                account.show_balance()
            elif choice == "4":
                old_pin = input("Enter your current PIN: ")
                new_pin = input("Enter your new PIN (4 digits): ")
                confirm_new_pin = input("Confirm your new PIN: ")
                if new_pin == confirm_new_pin and len(new_pin) == 4 and new_pin.isdigit():
                    account.change_pin(old_pin, new_pin, self.key)
                else:
                    print("PINs do not match or invalid PIN format.")
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid selection.")
            self.accounts[account_number] = {'pin': account.pin, 'balance': account.balance}
            save_accounts(self.accounts, self.key)

    def select_transaction(self):
        print("Please select a transaction:")
        print("1: Deposit")
        print("2: Withdraw")
        print("3: Check Balance")
        print("4: Change PIN")
        print("5: Exit")
        choice = input("Enter choice (1-5): ")
        return choice

# Main program starts here
def main():
    key = load_key()
    atm = ATM(key)

    while True:
        print("Welcome to the ATM")
        print("1: Create an account")
        print("2: Access your account")
        print("3: Exit")
        user_choice = input("Please select an option (1-3): ")
        if user_choice == "1":
            atm.create_account()
        elif user_choice == "2":
            user_account_number = atm.attempt_login()
            if user_account_number:
                atm.execute_transaction(user_account_number)
        elif user_choice == "3":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()

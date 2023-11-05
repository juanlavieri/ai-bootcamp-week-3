# make_withdrawal.py

def make_withdrawal(account):
    amount = float(input("Enter the amount to withdraw: "))
    account.withdraw(amount)

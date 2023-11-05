""" Create a SavingsAccount and CD class with methods"""

class SavingsAccount:
    """Creating a Savings Account class with parameters and methods"""
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    # This method gets the balance of the savings account.
    def get_balance(self):
        """Gets the balance for the savings account"""
        return self.balance

    # This method gets the interest rate of the savings account.
    def get_interest(self):
        """Gets the interest rate for the savings account"""
        return self.interest_rate

class CD(SavingsAccount):
    """Creating a CD Account class with parameters and methods"""
    def __init__(self, balance, interest_rate, months):
        # Call the parent class's __init__ method and pass the required arguments
        SavingsAccount.__init__(self, balance, interest_rate)
        self.months = months

    # This method gets the length of months for the CD.
    def get_months(self):
        """Gets the length of the CD"""
        return self.months

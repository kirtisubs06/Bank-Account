#################################################################
# Course: CS 3B Intermediate Software Design in Python
# Name: Kirti Subramanian
# Topic: Object-Oriented Programming
# Description: Tests the BankAccount class that models a simple bank account with deposit,
# withdrawal, and interest functionalities.
# Filename: kirtiSubramanianLab2.py
# Date: 7/25/2023
#################################################################

from decimal import Decimal
from kirtiSubramanianBank import BankAccount


def test_bank_account():
    # Instantiate a bank account with an original balance of $1000.00
    account = BankAccount(initial_balance=Decimal("1000.00"))

    # Deposit $500.00
    account.deposit(Decimal("500.00"))

    # Withdraw $2000.00
    account.withdraw(Decimal("2000.00"))

    # Adds 1% interest
    account.add_interest(1)

    # Adds 2% interest
    account.add_interest(2)

    # Deposit $125,000.99
    account.deposit(Decimal("125000.99"))

    # Withdraw $0.99
    account.withdraw(Decimal("0.99"))

    # Withdraw $126,500.00
    account.withdraw(Decimal("126500.00"))

    # Withdraw $10.00
    account.withdraw(Decimal("10.00"))

    # Adds 1% interest
    account.add_interest(1)

    # Show the account balance after each action.
    balance = account.get_balance()
    print(f"Final balance: {account._format_currency(balance)}")


if __name__ == "__main__":
    test_bank_account()


# output of this test run:
"""
/Users/kirtisubramanian/PycharmProjects/CS_3B_Summer_23/venv/bin/python /Users/kirtisubramanian/PycharmProjects/CS_3B_Summer_23/kirtiSubramanianLab2.py 
Current balance: $1,500.00
Current balance: $1,490.00
Current balance: $1,504.90
Current balance: $126,505.89
Current balance: $126,504.90
Current balance: $4.90
Looks like your funds are running low! Make sure to save soon.
Current balance: $-5.10
Uh oh! Looks like you're in debt. You must stop spending now and save money.
Final balance: $-5.10

Process finished with exit code 0
"""
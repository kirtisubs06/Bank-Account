#################################################################
# Course: CS 3B Intermediate Software Design in Python
# Name: Kirti Subramanian
# Topic: Object-Oriented Programming
# Description: Simulates a simple bank account with deposit, withdrawal, and interest functionalities.
# Additional text is outputted for the user, so they have feedback on their spending habits.
# Filename: kirtiSubramanianBank.py
# Date: 7/25/2023
#################################################################

from decimal import Decimal, ROUND_HALF_UP
import datetime  # Add this line to import the datetime module


class BankAccount:
    """
    BankAccount Class - Simulates a simple bank account with deposit, withdrawal, and interest functionalities.
    Uses the `decimal` module for accurate currency calculations.
    """
    OVERDRAFT_FEE = Decimal(10.0)

    def __init__(self, initial_balance=Decimal("0.0")):
        """
        Constructor for BankAccount.

        Parameters:
            initial_balance (Decimal): The initial account balance. Default is Decimal("0.0").
        """
        self.balance = initial_balance
        self.last_interest_date = None

    def deposit(self, amount):
        """
        Deposits money into the account.

        Parameters:
            amount (Decimal): The amount to be deposited.

        Returns:
            None
        """
        if amount > 0:
            self.balance += amount
            self._print_balance()

    def withdraw(self, amount):
        """
        Makes a withdrawal from the account or charges a penalty if sufficient funds are not available.

        Parameters:
            amount (Decimal): The amount to be withdrawn.

        Returns:
            None
        """
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                self.balance -= self.OVERDRAFT_FEE
            self._print_balance()

    def add_interest(self, rate):
        """
        Adds interest once monthly to a positive account balance.
        The rate parameter represents the current rate of interest (1% <= rate <= 2%).

        Parameters:
            rate (int): The interest rate to be applied.

        Returns:
            None
        """
        if 1 <= rate <= 2:
            if not self.last_interest_date or self.last_interest_date.month != self._get_current_month():
                interest_amount = self.balance * Decimal(rate) / Decimal(100)
                self.balance += interest_amount
                self.last_interest_date = self._get_current_date()
                self._print_balance()

    def get_balance(self):
        """
        Returns the current account balance.

        Returns:
            Decimal: The current account balance.
        """
        return self.balance

    def _get_current_date(self):
        """
        Gets the current date and time.

        Returns:
            datetime.datetime: The current date and time.
        """
        return datetime.datetime.now()

    def _get_current_month(self):
        """
        Gets the current month.

        Returns:
            int: The current month (1 to 12).
        """
        return self._get_current_date().month

    def _print_balance(self):
        """
        Prints the current account balance along with some feedback if needed.
        """
        formatted_balance = self._format_currency(self.balance)
        print(f"Current balance: {formatted_balance}")
        if self.balance < 0:
            print("Uh oh! Looks like you're in debt. You must stop spending now and save money.")
        elif self.balance <= 10:
            print("Looks like your funds are running low! Make sure to save soon.")

    def _format_currency(self, amount):
        """
        Formats the given amount as currency.

        Parameters:
            amount (Decimal): The amount to be formatted.

        Returns:
            str: The formatted currency string.
        """
        return "${:,.2f}".format(amount.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))

# Bank Account Simulator

## Course Information
- **Course**: CS 3B Intermediate Software Design in Python
- **Student**: Kirti Subramanian
- **Date**: 7/25/2023
- **Topic**: Object-Oriented Programming
- **Filename**: kirtiSubramanianBank.py

## Program Description
This Python script simulates a simple bank account, allowing users to manage their finances with basic functionalities like deposits, withdrawals, and accruing interest. The program provides feedback to users about their spending habits, encouraging responsible financial management. It uses the `decimal` and `datetime` modules for accurate currency calculations and date handling.

## Features

**Financial Transactions:**
- Deposit money into the bank account.
- Withdraw money with overdraft protection.
- Monthly interest accrual on the account balance.

**User Feedback:**
- Provides textual feedback on spending habits based on the account balance.
- Warnings for low balance and overdraft situations.

**Accurate Calculations:**
- Uses the `Decimal` class for precise currency calculations.
- Handles dates and months for interest calculation using the `datetime` module.

**Modular Design:**
- The program is structured with clear methods for each functionality, enhancing readability and maintainability.

## Installation

No additional installation is required, as the script uses standard Python libraries.

## Usage

To use the script, create an instance of the `BankAccount` class and call its methods:

```python
from kirtiSubramanianBank import BankAccount
from decimal import Decimal

# Create a bank account with an initial balance
account = BankAccount(Decimal("100.0"))

# Deposit money
account.deposit(Decimal("50.0"))

# Withdraw money
account.withdraw(Decimal("20.0"))

# Add interest
account.add_interest(1)  # 1% interest rate

# Check balance
print("Final balance:", account.get_balance())

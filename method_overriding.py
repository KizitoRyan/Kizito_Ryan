#Parent class: BankAccount
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

#Child class: SavingsAccount
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 50000:
            print("Withdrawal limit exceeded for savings account (max 50000).")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn from savings. New balance: {self.balance}")
        else:
            print("Insufficient funds in savings account.")

#Child class: BusinessAccount
class BusinessAccount(BankAccount):
    def withdraw(self, amount):
        fee = 100  
        total = amount + fee
        if total <= self.balance:
            self.balance -= total
            print(f"{amount} withdrawn from business account with a fee of {fee}. New balance: {self.balance}")
        else:
            print("Insufficient funds in business account.")

# Sample accounts
savings = SavingsAccount("Alice", 100000)
business = BusinessAccount("Bob", 200000)

# Test withdrawals
savings.withdraw(60000)     # Exceeds savings limit
savings.withdraw(40000)     # Valid
business.withdraw(50000)    # Includes fee

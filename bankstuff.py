import random

# Extend the BankAccount class
class BankAccount:
    def __init__(self, owner, has_overdraft=False):
        self.owner = owner
        self.balance = 0.0
        self.account_no = random.randint(111111111, 999999999)
        self.has_overdraft = has_overdraft
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("Deposit amount must be positive.")
            return self.balance
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance or self.has_overdraft:
                self.balance -= amount
                return self.balance
            else:
                print("Insufficient funds.")
                return self.balance
        else:
            print("Withdrawal amount must be positive.")
            return self.balance
    
    def __str__(self):
        return f"Account {self.account_no} - Balance: {self.balance:.2f}"


# Create the SavingsAccount class that subclasses BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, owner, has_overdraft=False):
        super().__init__(owner, has_overdraft)
    
    def withdraw(self):
        print("No withdrawals permitted")
        return self.balance


# Test the classes
# Create instances of BankAccount and SavingsAccount
checking = BankAccount("Alice", has_overdraft=True)
savings = SavingsAccount("Bob")

# Test deposits and withdrawals for BankAccount
print("Checking Account:")
print(checking)
checking.deposit(500)
print(f"After deposit: {checking}")
checking.withdraw(200)
print(f"After withdrawal: {checking}")
checking.withdraw(500)  # Should be allowed due to overdraft
print(f"After withdrawal with overdraft: {checking}")

# Test SavingsAccount
print("\nSavings Account:")
print(savings)
savings.deposit(500)
print(f"After deposit: {savings}")
savings.withdraw()  # Should not change balance and print message
print(f"After withdrawal attempt: {savings}")

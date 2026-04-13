class InsufficientFundsError(Exception):
    """Exception raised for errors in the withdrawal process."""
    def __init__(self, balance, amount):
        super().__init__(f"Insufficient funds: attempted to withdraw {amount}, but only {balance} available.")
        self.balance = balance
        self.amount = amount 

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance 

# Example usage
try:
    account = BankAccount(100)
    new_balance = account.withdraw(1)
    print(f"New balance: {new_balance}")
except InsufficientFundsError as e:
    print(e)


class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount 
            print(f"Withdrew: ${amount}. New balance: ${self.__balance}") 
        else:
            print("Invalid withdrawal amount!")

my_account = BankAccount()
my_account.deposit(100)
my_account.withdraw(10)
# print(my_account.__balance) # This would raise an AttributeError
class BankAccount:
     
    def __init__(self,account_number,balance):
        self.__balance = balance
        self.__account_number = account_number

    def deposit(self, amount):
        self.__balance += amount
        print(f"deposit of {amount} successful and balance is {self.__balance}")

    def withdraw(self, amount):
        self.__balance -= amount
        print(f"withdrawal of {amount} successful and balance is {self.__balance}")
    def get_balance(self):
        return self.__balance

account = BankAccount(123456789, 5000)
account.deposit(1000)
account.withdraw(2000)
account.get_balance()


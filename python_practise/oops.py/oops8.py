class Bank:
    def __init__ (self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
    
    def deposit(self, amount):
        print("Depositing amount:", amount)
        self.balance+=amount
        print("Balance after deposit:", self.balance)

    def withdraw(self, amount):
        print("Withdrawing amount:", amount)
        self.balance-=amount
        print("Balance after withdraw:", self.balance)

    def check_balance(self):
        return self.balance
    
b1=Bank(1000, "123456789")
b1.deposit(500)  # Output: Depositing amount: 500
b1.withdraw(200) # Output: Withdrawing amount: 200
print("Current balance:", b1.check_balance())  # Output: Current balance: 1300
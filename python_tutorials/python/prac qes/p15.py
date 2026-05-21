class Bank:
    bank_name="SBI"
    def __init__(self,acc_name,acc_no,balance):
        self.acc_name=acc_name
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited amount is",amount,"\n")
        print(f"the amount after credited{self.balance}\n")
    def withdraw(self,amount):
        self.balance-=amount
        print("withdraw amount is",amount,"\n")
        print(f"the amount after debited{self.balance}\n")
    def display(self):
        print("Account name is",self.acc_name,"\n")
        print("Account number is",self.acc_no,"\n")
        print("Account balance is",self.balance,"\n")
        print("Bank name is",Bank.bank_name,"\n")
b1=Bank("marco",123456789,5000)
b1.deposit(1000)
b1.withdraw(2000)
b1.display()
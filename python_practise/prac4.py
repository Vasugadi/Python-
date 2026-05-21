class Bank:
    BankName = "Global Bank"
    BankLocation = "New York"

    def __init__(self,acc,balance):
        self.accNo = acc
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")
        
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance is {self.balance}")
        else:
            print("Insufficient balance")

    def display(self):
        print(f"Account Number: {self.accNo}")
        print(f"Balance: {self.balance}")
    
# Driver code
b1 = Bank(123456789,1000)
b1.deposit(500)
b1.withdraw(2000)
b1.display()

        
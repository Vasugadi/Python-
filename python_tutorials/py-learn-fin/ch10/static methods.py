# methods that dont use the self parameter are called static methods
# work at class level 

class Math:
    @staticmethod
    def add(x,y):
        return x+y

    @staticmethod
    def subtract(x,y):
        return x-y

    @staticmethod
    def multiply(x,y):
        return x*y

    @staticmethod
    def divide(x,y):
        return x/y

print(Math.add(2,3))
print(Math.subtract(2,3))
print(Math.multiply(2,3))
print(Math.divide(2,3))


#abstraction : hiding the implementation details of a class and only showing the essential features to the user
#encapsulation : binding the data and methods that manipulate the data into a single unit called class
#inheritance : allows a class to inherit attributes and methods from another class
#polymorphism : allows objects of different classes to be treated as objects of a common superclass
#abstraction
class Car:
    def __init__(self):
        self.acc=False
        self.brk = False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started..")


car1=Car()
car1.start()

#encapsulation
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
    
    #debit 
    def debit(self,amount):
        self.balance-=amount
        print("amount debited",amount)
        print("balance is",self.balance)

    def credit(self,amount):
        self.balance=+amount
        print("amount credited",amount)
        print("balance is",self.balance)
    def get_balance(self):
        return self.balance
    
account1=Account(1000,"1234567890")
account1.debit(500)
account1.credit(500)


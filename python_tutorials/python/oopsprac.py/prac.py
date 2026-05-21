class Sub:
     colleg="jntu"
     def __init__(self,marks):
         self.marks=marks
     def avg(self):
          sum=0
          for i in self.marks:
              sum+=i
          return sum/len(self.marks)
     
s1=Sub([10,20,30,40,50])
print(s1.avg())
     
     
#static method
class Sub:
     colleg="jntu"
     def __init__(self,marks):
         self.marks=marks
     def avg(self):
          sum=0
          for i in self.marks:
              sum+=i
          return sum/len(self.marks)
     @staticmethod
     def staticmethod():
         print("this is static method")

s1=Sub([10,20,30,40,50])
print(s1.avg())
#s1.staticmethod() if decorator is written then we can call it by object
Sub.staticmethod()   
#class method
class Sub:
     colleg="jntu"
     def __init__(self,marks):
         self.marks=marks
     def avg(self):
          sum=0
          for i in self.marks:
              sum+=i
          return sum/len(self.marks)
     @staticmethod
     def staticmethod():
         print("this is static method")
     @classmethod
     def classmethod(cls):
         print("this is class method")

s1=Sub([10,20,30,40,50])
print(s1.avg())
s1.staticmethod()
s1.classmethod()


class Bank:
    bank_name="ssbi"
    def __init__(self,acc_no,acc_name,balance):
        self.acc_no=acc_no
        self.acc_name=acc_name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("amount deposited")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print("amount withdrawn")
        else:
            print("insufficient balance")
    def balance(self):
        print("balance is",self.balance)
    
b1=Bank(123456789,"sai",10000)
b1.deposit(5000)
b1.withdraw(2000)
print(b1.bank_name)

# del s1.name it deletes the name attribute of s1 object
# del s1 it deletes the s1 object

# class method is used to change the class variable

#private attributes and public attributes
#private attributes can be accessed only within the class
#public attributes can be accessed from anywhere
class Stud:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__name=name #it became private attribute
    def display(self):
        print("name is",self.name)
        print("age is",self.age)
    def reset_pass(self):
        self.__name="sai"
        print(self.__name)
s1=Stud("sai",20)  
s1.reset_pass() 


class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")
class Toyata(Car):
    def __init__(self,name,type):
        self.name=name
        self.type=type
        super().__init__(type)


class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,other):
        return Complex(self.real+other.real,self.imag+other.imag)


class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius
c1=circle(5)
print(c1.area())
print(c1.perimeter())
    
print(c1.radius)

class Employee:
    def __init__(self,role,dept):
        self.role=role
        self.dept=dept
        
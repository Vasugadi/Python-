# create class which is the blueprint of an object
class Employee:
    Name="Vasu"
    age=20
harry=Employee() #creating an object/instance of a class
print(harry.Name)
print(harry.age)

# creating a class with conustroctor
# all classes have the function called _init_() which is called the constructor
# it is called when an object is created from a class and it allows the class to initialize the attributes of the class
class Employee:
    def __init__(self,name,age):
        self.Name=name
        self.age=age

    def printdetails(self):
        return f"the name of the employee is {self.Name} and age is {self.age}"
harru=Employee("harry",20)
vasu=Employee("vasu",20)
print(harru.printdetails())

class Student:
    name="vasu"
    age=20
    def __init__(self,name,age):
        self.Name=name
        self.age=age
    def printdetails(self):
        return f"the name of the employee is {self.Name} and age is {self.age}"
vasu=Student("vasu",20)
print(vasu.printdetails())

# attributes are nothing but data stored in variables
# methods are functions which are defined inside a class

class Student:
    def __init__(self,name,age):
        self.Name=name
        self.age=age
    def printdetails(self):
        return f"the name of the employee is {self.Name} and age is {self.age}"
vasu=Student(["vasu","harry"],20)
vasu.Name=["vasu","harry"]
print(vasu.printdetails())
# we can also add attributes to a class after it is created
# we can also add methods to a class after it is created

#default parameters
class Student:
    name="vasu"
    def __init__(self):
        pass
    def __init__(self,name,age=20):
        self.Name=name
        self.age=age
    def printdetails(self):
        return f"the name of the employee is {self.Name} and age is {self.age}"
vasu=Student("vasu",20)
print(vasu.printdetails())

#class and isinstance attrinutes
class Student:
    name="vasu"
    def __init__(self,name,age):
        self.Name=name
        self.age=age
    def printdetails(self):
        return f"the name of the employee is {self.Name} and age is {self.age}"
    
v=Student("vasu",80)
print(v.name)
print(isinstance(v,Student))
print(v.age)
print(v.printdetails())
print(Student.name) # accessing class attribute

# class attribute is taken by all the objects of the class
# instance attribute is taken by only the object of the class

class Students:
    cname="xyz"
    # create a constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def printAVG(self):
        sum=0
        for val in self.marks:
            sum+=val

        return sum/len(self.marks)
        print(f"the average marks of {self.name} is {marks/len(self.marks)}")

harry=Students("harry",[60,80,90])
harry.printAVG()
Students.cname# accessing class attribute


# static method that dont use the self parameter (work at class level)
# class method that use the cls parameter (work at class level)
class Employee:
    cname="xyz"
    # create a constructor
    def __init__(self,emp_id):
        self.emp_id=emp_id

    def printDetails(self,name):
        print(f"the name of the employee is {name} and emp id is {self.emp_id}")
    
    @staticmethod
    def welcome():
        print("welcome to xyz company")

E1=Employee(1)
E1.printDetails("harry")
E1.welcome()
Employee.welcome()
print(Employee.cname)

# abstraction hides the actual implementation of the class  and give only essential code
class Car:
    def __init__(self):
        self.clutch=False
        self.acc=False
    def Start_Car(self):
        self.clutch=True
        self.acc=True
        print("car started")
    def Stop_Car(self):
        self.clutch=False
        self.acc=False
        print("car stopped")
h1=Car()
h1.Start_Car()
h1.Stop_Car()

#wrapping data and fucntion into a single unit(object)

class Bank:
    Bankname="Sbi"
    def __init__(self,accno,name,balance):
        self.accno=accno
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"the amount {amount} is deposited to {self.name} account")
        print("total bal",self.checkbalance())
    def withdraw(self,amount):
        self.balance-=amount
        print(f"the amount {amount} is withdrawn from {self.name} account")
        print("the total bal",self.checkbalance())

    def checkbalance(self):
        return self.balance
a1=Bank(123456789,"harry",1000)
a1.deposit(1000)
a1.withdraw(1000)



# del keyword to del object properties or object itself 
#del s1.name
# del s1

class Vasu:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Vasu("vasu",20)
print(s1)
print(s1.name)
#to delete s1
del s1.name
# after deletion of s1 we cant access s1.name
#print(s1.name)

# Private(like) attribute & methods
# these are attributes and methods that are not accessible outside the class
# we can access them by using _classname__attribute
class Account:
    def __init__(self,accno,accpass):
        self.accno=accno
        self.accpass=accpass
acc1=Account(123456789,1234)
print(acc1.accno)
print(acc1.accpass)
acc1.accpass=12345
print(acc1.accpass)

####
# to make something private we keep that thing in private
# by adding __ before the attribute name
class Account:
    def __init__(self,accno,accpass):
        self.accno=accno
        self.__accpass=accpass
    def reset_pass(self): # it can work here bcz its in class
        print(self.__accpass)

acc1=Account(123456789,1234)
print(acc1.accno)
# print(acc1.__accpass)# this will give error
print("this is private",acc1._Account__accpass)# this will work
print(acc1.reset_pass())

###########
class Person:
    __name="harry"
p1=Person()
print(p1._Person__name)

########
class Students:
    __name="anonymous"

    def __hello(self):
        print("hello")
    @staticmethod
    def welcome():
        print("welcome to xyz company")
    def wel(self):
        self.__hello()
p1=Students()
print(p1._Students__name)
p1._Students__hello()
p1.welcome()
p1.wel()

# inheritance
# it is a mechanism of creating a new class from an existing class
# the new class is called derived class and the existing class is called base class
# the derived class inherits all the properties and methods of the base class
# the derived class can also add its own properties and methods
class Car:
    color="black"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class ToyataCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyataCar("toyata")
car1.start()
car1.stop()
print(Car.color)
print(car1.name)
print(car1.color)

#single inheritance ---> base class ----> derived class
#multilevel inheritance ---> base class ----> derived class ----> derived class
#multiple inheritance ---> derived class ----> base class1 ----> base class2

class Car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class TeslaCar(ToyotaCar):
    def __init__(self, type):
        self.type=type

car1=TeslaCar("tesla")
car1.start()
car1.stop()
print(car1.brand)
print(car1.type)

#multiple inheritance
class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C(A,B):
    varc="welcome to class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varc)

#####
#super method to access the methods of the parent class
# super --parent  we are inheriting
class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        super().start()
        super().stop()
        self.name=name
car1=Car("pairus","ele")
print(car1.type)

## class method
class Person:
    name="anonymous"

    def changeName(self,name):
        Person.name=name
p1=Person()
print(p1.name)
p1.changeName("harry")
print(p1.name)
print(Person.name)
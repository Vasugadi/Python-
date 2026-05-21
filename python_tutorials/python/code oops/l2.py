class Person:
    name="anonymous"

    def changeName(self,name):
        Person.name=name
p1=Person()
print(p1.name)
p1.changeName("harry")
print(p1.name)
print(Person.name)

###########
class Person:
    name="anonymous"

    def changeName(self,name):
        self.__class__.name="rahul"
p1=Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)

###########
class Person:
    name="anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name=name
p1=Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)



class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.perc=str((self.phy+self.chem+self.math)/3)+"%"
    def calcPercentage(self):
        self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

p1=Student(60,80,90)
print(p1.perc)
p1.phy=90
print(p1.phy)
p1.calcPercentage()
print(p1.perc)


class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
s1=Student(60,80,90)
print(s1.percentage)
s1.phy=90
print(s1.percentage)

#polymorphism
#a.__add__(b) ---->means a+b
#b.__add__(a) ---->means b+a
# to write a complex number
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def shownum(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return Complex(newreal,newimg)
num1=Complex(3,4)
num1.shownum()
num2=Complex(5,6)
num2.shownum()
num3=num1+num2

num3.shownum()
#oop in python 
#to map with real world scenarios we started objects in code
#this is called object oriented programming

#class is a blueprint of an object


#creating a class
class Employee:
    name="nivin pauly"

s1=Employee()
print(s1.name)
s1.name="nivin"
print(s1.name)

#creating a class 
class Car:
    color="red"
    brand="bmw"
    model="x5"
    price=1000000

c1=Car()
print(c1.color)
print(c1.brand)
print(c1.model)
print(c1.price)


#conustructor
class Student:
    name="bmw"
    def __init__(self,brand):
        self.brand=brand
        print("constructor called")
    
    def 

s1=Student("bmw")
print(s1.brand)
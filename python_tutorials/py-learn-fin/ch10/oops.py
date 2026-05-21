#to map with real world scenarios with we use object this is nothing but oops
#procedural coding is nothing but writing code in a sequence of steps to solve the problem
num=int(input("enter number: "))
num2=int(input("enter number: "))
sum=num+num2
print(sum)

#onject---1.class--2.object
#class is a blueprint of an object
#object is an instance of a class
#class is a user defined data type
#class is a template for creating objects
#class is a collection of objects

#creating a class
class car:
    name="bmw"

#creating an object
c1=car()
print(c1.name)

#class is a blueprint of an object
class bike:
    name="yamaha"
    color="red"
    price=100000
    model="yamaha FZ"
#creating an object
b1=bike()
print(b1.name,b1.color,b1.price,b1.model)
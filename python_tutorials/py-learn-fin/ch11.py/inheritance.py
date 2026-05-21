# when one class (child/derived) derives the properties and methods of another class (parent/base)

class Car:

    @staticmethod
    def car_start():
        print("This is a car")
    @staticmethod
    def car_stop():
        print("This is a car color")
   
class BMW(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(BMW):
    def __init__(self,type):
        self.type = type


car1=BMW("BMW")
print(car1.name)
print(car1.car_start())
print(car1.car_stop())

# inheritance is a way to form new classes using classes that have already been defined. The new classes will have some of the same properties as their parent classes and will also have the ability to define new properties of their own.
# there are three different kinds of inheritance
# single inheritance
# multiple inheritance
# multilevel inheritance
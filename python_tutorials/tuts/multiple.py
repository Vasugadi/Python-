#multiple inheritance
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def drive(self):
        print(f"{self.name} is driving")

class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def ride(self):
        print(f"{self.name} is riding")

class CarBike(Car, Bike):
    def __init__(self, name, color):
        Car.__init__(self, name, color)
        Bike.__init__(self, name, color)

    def drive(self): #method overriding
        print(f"{self.name} is driving in {self.color} color")

c = CarBike("CarBike", "Black")
c.drive()
c.ride()
print(c.name, c.color)
#output:
#CarBike is driving in Black color
#CarBike is riding
#CarBike Black
#method overriding
#method overriding is when a child class has the same method as the parent class and it overrides the parent class method
#method overloading
#method overloading is when a class has multiple methods with the same name but different parameters
#multiple inheritance
#multiple inheritance is when a class inherits from multiple classes



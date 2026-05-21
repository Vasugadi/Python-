#del keyword : to delete object properties or object itself

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

car1 = Car("BMW", "Black")
car2 = Car("Audi", "White")
print(car1.name, car1.color)
print(car2.name, car2.color)

del car1.name
print(car1.name) #AttributeError: 'Car' object has no attribute 'name'
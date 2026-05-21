# abstraction is nothing hiding the compelx details from the user
# we can achieve abstraction using abstract class and abstract method

from abc import ABC, abstractmethod

class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        pass

class AnotherSubclass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print("The subclass is doing something")

x = AnotherSubclass()
x.do_something()

# abstract classes cannot be instatiated
# x = AbstractClassExample() # Raises error
#child class must implement the abstract method of parent class

from abc import ABC abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(vehicle):
    def start(self):
        print("Car is starts by key")
class Bike(vehicle):
    def start(self):
        print("Bike is starts by kick")
        
car=Car()
car.start()

bike=Bike()
bike.start()

# poly: one name multiple forms
# encap: hiding data and allowing controlled access
# inherit: reuse properties / methods from parent class
# abstr: hide the details and show the essential
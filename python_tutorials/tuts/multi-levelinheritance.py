class Car:
    @staticmethod
    def start():
        print("car started")

class Bmw(Car):
    def __init__(self,brand):
        self.brand = brand
class Fortuner(Bmw):
    def __init__(self,model):
         self.model = model
    
car1=Fortuner("Fortuner")
car1.start()
print(car1.brand) # inherited from Bmw but not from Car so no output
print(car1.model) 

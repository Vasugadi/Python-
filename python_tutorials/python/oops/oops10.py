
#multi--- level inheritance
class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")
class ToyataCar(Car):
    def __init__(self,name):
        self.name=name
class Fortuner(ToyataCar):
    def __init__(self,type):
        self.type=type

        

car1=ToyataCar("toyata")
car2=Fortuner("Deisel")
print(car2.type)
car1.start()
car1.stop()
 
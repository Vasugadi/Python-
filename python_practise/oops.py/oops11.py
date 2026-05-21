class Car:
    def  __init__ (self,type):
        self.type = type
    
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")
class Toyota(Car):
    def __init__ (self,name,type):
        super().__init__(type)
        super().start()
        super().stop()
        self.name = name

t1 = Toyota("Camry","Sedan")
print(t1.name)
print(t1.type)
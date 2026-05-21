# super method
class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car is started")
    @staticmethod
    def stop():
        print("car is stopped")

class BMW(Car):
    def __init__(self,type,model):
        super().__init__(type)
        self.model=model
        super().start()
        super().stop()
c1=BMW("sedan","x5")
print(c1.type)
print(c1.model)
c2=Car("sedan")
c2.start()
c2.stop()
print(c2.type)
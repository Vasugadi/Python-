#single inheritance
class Car:
    @staticmethod
    def hello():
        print("hello")

class Bmw(Car):
    def __init__(self,name):
        self.name=name
    
c1=Bmw("bmw")
c1.hello()
print(c1.name)
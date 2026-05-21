#super method is used to call parent class method
class Car:
    def __init__(self,type="Vehicle"):
        self.type=type
        print("Car class constructor")
        
    @staticmethod
    def start():
        print("Car started")
class Toyata(Car):
    def __init__(self,model,year,type):
        super().__init__(type) #calling parent class constructor
        super().start() #calling parent class method
        self.model=model
        self.year=year
c2=Car()
print(c2.type)
c1=Toyata("Innova",2020,"SUV")
print(c1.model)
print(c1.year)
print(c1.type)
#super method is used to call parent class method
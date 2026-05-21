# class Car:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
#     def car_Details(self):
#         print(f"this car is {self.brand} and color is {self.color}")
        
# bmw=Car("bmw","red")
# print(bmw.car_Details()) 

# car2=Car("audi","black")
# print(car2.car_Details())    
        
        
class Car:
    def set_Details(self,brand,color):
        self.brand=brand
        self.color=color
    def show_Details(self):
        print(f"this car is {self.brand} and color is {self.color}")

bmw=Car()
bmw.set_Details("bmw","red")
bmw.show_Details()

car2=Car()
car2.set_Details("audi","black")
car2.show_Details()
    

"""   
1- default constructor (self)
2- parameterized constructor (self,brand,color)
3-  constructor with default values (self,name="unknown",age=0)
"""
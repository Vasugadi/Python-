class Car:
    @staticmethod
    def greet():
        print("Hello from static method")
        
    
class Tesla(Car):
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def show(self):
        print(f"Color: {self.color}, Model: {self.model}")
        
t1 = Tesla("Red", "Model S")
t1.show()   
t1.greet()  # Inherited static method
Tesla.greet()  # Calling static method from class
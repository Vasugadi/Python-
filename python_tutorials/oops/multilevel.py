class Car:
    @staticmethod
    def start():
        print("Car started")
        
    @staticmethod
    def stop():
        print("Car stopped")
        
class Toyota(Car):
    def __init__(self, model, year):
        self.model = model
        self.year = year

class Corolla(Toyota):
    def __init__(self, variant):
        self.variant = variant

    def display_info(self):
        print(f" Variant: {self.variant}")
        
c1 = Corolla("Sport")
c1.display_info()
c1.start()  # Inherited static method
c1.stop()   # Inherited static method
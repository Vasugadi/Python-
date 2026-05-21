class Car:
    color = "black"
    brand = "BMW"
class brand:
    name = "BMW"
    country = "Germany"
class scooty(Car, brand):
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Model: {self.model}, Year: {self.year}, Color: {self.color}, Brand: {self.brand}, Brand Name: {self.name}, Country: {self.country}")

scooty1 = scooty("Sport", 2022)
scooty1.display_info()
#multiple inheritance
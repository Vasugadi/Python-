#abstraction
class Student:
    def __init__(self):
        self.acc=False
        self.brake=False
        self.clutch=False

    def start(self):
        self.acc=True
        self.brake=True
        self.clutch=True
        print("Vehicle started")

s1=Student()
s1.start()  # Output: Vehicle started
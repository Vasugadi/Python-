class Car:
    def __init__(self):
        self.acc=False
        self.brake=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        if self.acc==True and self.brake==False and self.clutch==True:
            print("car started")
        else:
            print("car not started")
s1=Car()
s1.start()
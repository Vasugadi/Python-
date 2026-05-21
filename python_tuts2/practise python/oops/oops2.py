class Car():
    Car_brand = "bmw"
    def __init__(self,acc,brake):
        self.acc = acc
        self.brake = brake
        
    def start(self,acc,brake):
        print("car is started")
        if(acc == 0):
            print("car is not started")
        else:
            print("car is started")

    def stop(self,acc,brake):
        print("car is stopped")
        if(brake == 0):
            print("car is not stopped")
        else:
            print("car is stopped")
            
            
journey=Car(0,0)
print(journey.acc)
print(journey.brake)
journey.start(0,0)
journey.stop(0,0)

"""  
one name,many forms

run
person can run fast
car runs on petrol
computer program run smoothly

"""

print(len("hello"))
print(len([1,2,3,4,5]))
print(len({"A":1,"b":2,"c":3}))

#polymorphism with classes method overriding
class Bird():
    def sound(self):
        print("birds make sounds")
class Crow(Bird):
    def sound(self):
        print("crow makes Caw Caw")
        
class Parrot(Bird):
    def sound(self):  # 定义sound方法，用于描述鹦鹉的声音
        print("parrot makes Squeak Squeak")  # 打印鹦鹉发出的声音"parrot makes Squeak Squeak"
        
bird1=Crow()
bird2=Parrot()
bird1.sound()
bird2.sound()

#on operators
print(1+2)
print("1"+"2")
print([1,2]+[3,4])
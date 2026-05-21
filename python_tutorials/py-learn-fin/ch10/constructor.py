
class Student:
    #default constructor
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Student class constructor called")
    

s2=Student("John", 20)
print(s2.name,s2.age)

#the data stored inside variables are called attributes
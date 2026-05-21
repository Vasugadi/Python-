class Student:
    name="sai"
    def __init__(self,age):
        print("constructor")
        self.age=age
    def ag(self):
        print(self.age)
s1=Student(10)
print(s1.name)
print(s1.age)
s1.ag()
# print(Student.sum(10,28)) # its an example of class method

#default constructors
#parameterized constructors
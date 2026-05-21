#methods 
#methods are functions that belong to objects
class Student:
    def __init__(self, fullname):
        self.name = fullname
    def hello(self):#in parrenthesis we should mention self 
        print('Hello, my name is', self.name)
    

student1 = Student('John')
student1.hello()
print(student1.name)
#Hello, my name is John


class Student:
    def __init__(self, fullname,marks):
        self.name = fullname
        self.marks = marks
    def hello(self):
        print('Hello, my name is', self.name)
    def getmarks(self):
        return self.marks

student1 = Student('John', 90)
student1.hello()
print(student1.getmarks())

    
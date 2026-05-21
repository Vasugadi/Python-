# static method
class Student:
    college_name = "cbit"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    @staticmethod
    def hello():
        print("hello world")

    def get_name(self):
        return self.name

    def get_marks(self):
        return self.marks
    
s1=Student("marco",[90,80,70])
#college_name is a class variable
print(Student.college_name)#s1.college_name is an instance variable
s1.hello()
print(s1.get_name())
print(s1.get_marks())


#@ staticmethod is a decorator which is used to define a static method
# decorators are used to modify the behaviour of a function or class
# static methods are used when we don't need to access any instance variable or class variable

class Student:
    def __init__(self,fullname,marks):
        self.marks=marks
        self.name=fullname
#static method method is not bound to class or object
#it is bound to the namespace of the class
#these dont use the self parameter (works at class level)
    @staticmethod
    def greet():
        print("Hello from static method")
        
s1=Student("Karan",90)
s1.greet()
Student.greet()
s2=Student("Karanya",78)
s2.greet()
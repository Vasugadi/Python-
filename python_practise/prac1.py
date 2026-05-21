class Student:
    college="ABC College"
    
    #default constructor
    def __init__(self,fullname):
        pass
    
    #parameterized constructor
    def __init__(self,fullname):
        self.name=fullname
        print("Constructor is called")
        
    #create a method
    def wishes():
        print("Welcome to OOPs in Python")
    
    #create a method
    def showDetails(Self):
        print(f"Name: {Self.name}, College: {Self.college}, Address: XYZ")
    
    #static method: its not dependent on object or class we will call it directly
    @staticmethod
    def info():
        print("This is a Student class")
        
#create object
s1=Student("John Doe") #constructor is called
print(s1.name)  # Output: John Doe
print(Student.college)  # Output: ABC College and its an  class arttribute
#calling method
Student.wishes()  # Output: Welcome to OOPs in Python
s1.showDetails()  # Output: Name: John Doe, College: ABC College, Address: XYZ
Student.info()  # Output: This is a Student class00

s2=Student("Jane Smith")
print(s2.name)  # Output: Jane Smith
del s2.name
print(s2.name)  # AttributeError: 'Student' object has no attribute 'name'
del s1
print(s1.name)  # AttributeError: 'Student' object has no attribute 'name'
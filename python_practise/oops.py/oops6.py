#static method
class Student:
    def __init__(self,name):
        self.name=name
        
    @staticmethod
    def get():
        print("This is static method")


s1=Student("John")
s1.get()  # Output: This is static method
Student.get()  # Output: This is static method

    
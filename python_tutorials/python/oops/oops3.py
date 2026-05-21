class Student:
    # default constructors 
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self,age):
        # Initialize the age attribute of the object
        self.age=age
    def display(self):
        print("age is",self.age)
s1=Student(20)
print(s1.age)
s1.display()

# the data stored in variables is nothing but attributes
# the functions are nothing but methods
# the variables and methods are called as properties of the class

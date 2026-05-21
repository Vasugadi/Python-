#---------creating a class along with conustructor---------
class Student:
    #default constructor
    def __init__ (self):
        pass

    #para

    def __init__ (self,fullname): # Constructor __init__ is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        self.name=fullname
        # self.name is an instance variable, which means it is unique to each instance of the class. It is used to store the name of the student.
        #self is a reference to the current instance of the class, allowing access to its attributes and methods.
        #fullname is a parameter that is passed to the constructor when an object is created from the class. It is used to set the value of the name attribute.
        
s1=Student("John")
print(s1.name)  # Output: John
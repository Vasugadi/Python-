# the data storeed in var is called an attribute
#parameter is passed to the method
#argument is passed to the function
#self is used to access the attribute and method of class
#class.attr to access the class attribute
#object.attr to access the object attribute
#class.method to access the class method
#object.method to access the object method
#self.name,self.marks are called instance variable
#college name is called class variable
#class variable is shared by all the objects of the class
#instance variable is unique for each object

class Student:
    college="ABC" #class variable
    name="anonymous"
    #obj attr > class attr in priority
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    #methods
    def hello(self):
        print("Hello",self.name)
    
s1=Student("Karan",90)
s2=Student("Karanya",78)

print(s1.college)
print(s2.college)
print(Student.college)
print(s1.name)
print(s2.name)
print(s1.marks)
print(s2.marks)
print(s1.__dict__) #to see the attributes of the object
print(s2.__dict__) #to see the attributes of the object
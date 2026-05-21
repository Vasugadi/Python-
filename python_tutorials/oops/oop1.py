# function--redundancy decrease
# reusability--increase

# object oriented programming

# class -- blueprint
#method -- function inside class
# object -- instance of class

#creating a class
class Student:
    #attribute or property
    name="karan"
    def __init__(self,name):
        self.name=name
        
    def getname(self):
        return self.name
    
        
        
#creating a method
s1=Student("rahul")
print(s1.name)
print(Student.name)
print(s1.getname())


#class & instance attributes
# Class.attr
# obj.attr

#self.name ---- the name of every object is different
#self.age ---- the age of every object is different
# objects occupy space in the memory

# some times there will be some variable which are common to all the objects
# those variables are called as class attributes

class Employee:
    company = "Google" # class attribute
    location = "USA"
    name="anonymous" #class attribute   
    def __init__(self,name):
        self.name=name #obj attri > class attr

        
s1=Employee("mama")
print(s1.company,s1.location,s1.name)
# it can be written as
print(Employee.company,Employee.location)


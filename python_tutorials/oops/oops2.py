#constructor invokes during creation of object
#_init_ function is called constructor

#creation of class
class Student:
    #class attribute
    #name="Karan"
    #default constructor// these are called  if no constructor is defined automatically
    def __init__(self):
        pass
    
    #constructor
    #self parameter is used to access the attribute and method of class
    #parameterized constructor
    def __init__(self,fullname,marks):
        self.mar=marks
        self.name=fullname
       # print(self)
        #hence self parameter is used to access the attribute of class
        
        print("creating new student")

#object creation
s1=Student("Karanya",90)#constructor invokes
print(s1.name)
print(s1.mar)

s2=Student("Karan",78)#constructor invokes
print(s2.name)
print(s2.mar)



    
    
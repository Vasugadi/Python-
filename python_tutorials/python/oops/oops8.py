# private(like) attributes and methods
# conceptual implementation in python

# Private attribute and methods are meant to be used only within the class 
# and are not accesible from outside the class

# public  : we access from outside the class
class Student:
    def __init__(self,name):
        self.name=name
    
s1=Student("shradha")
print(s1.name)

# private :
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset(self):
         print(self.__acc_pass)

acc1=Account("12345","Abcde")
print(acc1.acc_no)
acc1.reset()

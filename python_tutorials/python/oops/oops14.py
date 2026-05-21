#@ property -- we use property decorator on any method in the class to use the mehtod as a property
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    def ch(self):
        self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

stu1=Student(45,67,89)
print(stu1.percentage)
stu1.phy=78
print(stu1.phy)
stu1.ch()
print(stu1.percentage)



class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"

stu1=Student(45,67,89)
print(stu1.percentage)
stu1.phy=78
print(stu1.percentage)


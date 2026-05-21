class Student:
    def __init__(self,name,phy,chem,math):
        self.name=name
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    def calculate(self):
        return (self.phy+self.chem+self.math)/3
    
stu1=Student("Karan",90,80,70)
print(stu1.percentage)
print(stu1.calculate())
stu1.phy=100
print(stu1.percentage)
print(stu1.calculate())

#we use property decorator on any method in the class to use the method as a property


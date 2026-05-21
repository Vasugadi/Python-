class   Student:
    def __init__(self,name,age,phy,chem,math):
        self.__name=name
        self.__age=age
        self.phy=phy
        self.chem=chem
        self.math=math
    
    @property
    def perc(self):
        return (self.phy+self.chem+self.math)/3
    
stu1=Student("Rahul",20,90,80,70)
print(stu1.perc)
stu1.phy=80
print(stu1.perc)
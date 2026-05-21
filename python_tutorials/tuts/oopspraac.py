class student:
    college_name="amity"
    def __init__(self,math,phy,chem):
        self.math=math
        self.phy=phy
        self.chem=chem
    def calc_avg(self):
        self.avg=(self.math+self.phy+self.chem)/3
        return self.avg
    
    def display(self):
        print("math=",self.math)
        print("phy=",self.phy)
        print("chem=",self.chem)
        print("avg=",self.avg)
        print("college name=",student.college_name)

math=int(input("enter math="))
phy=int(input("enter phy="))
chem=int(input("enter chem="))

s=student(math,phy,chem)
s.calc_avg()
s.display()

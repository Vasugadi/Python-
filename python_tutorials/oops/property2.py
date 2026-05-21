class Students:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property
    def percentage(self):
        return (self.phy+self.chem+self.math)/3
    
s=Students(90,80,70)
print(s.percentage)
s.phy=100
print(s.percentage)
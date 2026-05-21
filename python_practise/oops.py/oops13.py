class Student:

    def __init__ (self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.total = self.phy + self.chem + self.math

    def the_total(self):
        return self.phy + self.chem + self.math
    
s1=Student(80, 90, 85)
print(s1.total)  # Output: 255
print(s1.the_total())  # Output: 255

s1.phy = 95
print(s1.total)  # Output: 280
print(s1.the_total())  # Output: 270


############instead we can use the property method to make it more elegant
class Student:

    def __init__ (self,phy,chem,math):
        self._phy = phy
        self._chem = chem
        self._math = math

    @property
    def total(self):
        return self._phy + self._chem + self._math


s1=Student(80, 90, 85)
print(s1.total)  # Output: 255
s1._phy = 95
print(s1.total)  # Output: 255 (still returns the original total)
s1._chem = 100 # 
print(s1.total)  # Output: 265 (updated total with new chemistry score)
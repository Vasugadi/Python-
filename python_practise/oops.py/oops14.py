class Complex:
    def  __init__ (self,real,img):
        self.real=real
        self.img=img
    
    def show(self):
        print(self.real,"i +",self.img,"j")

    def add(self,other):
        print(other.real, "i +", other.img, "j")
        new_real = self.real + other.real
        new_img = self.img + other.img
        return Complex(new_real, new_img)


c1=Complex(2,3)
c1.show()  # Output: 2 i + 3 j
c2=Complex(4,5)
c2.show()  # Output: 4 i + 5 j
c3=c1.add(c2)
c3.show()

# we can use dunder function to remove the new function

class Complex:
    def  __init__ (self,real,img):
        self.real=real
        self.img=img
    
    def show(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self, other):
        new_real = self.real + other.real
        new_img = self.img + other.img
        return Complex(new_real, new_img)
    
    def __sub__ (self,other):
        new_real = self.real - other.real
        new_img = self.img - other.img
        return Complex(new_real, new_img)
    
    


c1=Complex(2,3)
c1.show()  # Output: 2 i + 3 j
c2=Complex(4,5)
c2.show()  # Output: 4 i + 5 j
c3=c1+c2
c3.show()
# Output: 6 i + 8 j
c4=c1-c2
c4.show()
# Output: -2 i + -2 j


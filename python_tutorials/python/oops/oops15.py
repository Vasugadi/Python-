#polymorphism: operator overloading 
# its an ability to use the same operator for different types of data
# one has many forms
 
1+2 #addition
print(type(1))

print("Apna"+"college")#concatenat
print(type("Apna"))#string

print([1,2,3,4]+[4,5,6])#merge
print(type([1,2,3,4]))#list

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def show(self):
        print(self.real,"i+",self.imag,"j")
    #without dunder function
    def add(self,num2):
        real=self.real+num2.real
        imag=self.imag+num2.imag
        return Complex(real,imag)

num1=Complex(1,3)
num2=Complex(2,4)
num3=num1.add(num2)
num3.show()
num1.show()
num2.show()

#with dunder function
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def show(self):
        print(self.real,"i+",self.imag,"j")

    def __add__(self,num2):
        real=self.real+num2.real
        imag=self.imag+num2.imag
        return Complex(real,imag)

    def __sub__(self,num2):
        real=self.real-num2.real
        imag=self.imag-num2.imag
        return Complex(real,imag)

num1=Complex(1,3)
num2=Complex(2,4)
num3=num1+num2
num3.show()
num1.show()
num2.show()
num4=num1-num2
num4.show()

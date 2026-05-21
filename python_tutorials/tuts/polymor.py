class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def showNumber(self):
        print(self.real,"i+ ",self.imag,"j")

    def  __add__(self, other):
        newReal=self.real+other.real
        newImag=self.imag+other.imag
        return Complex(newReal,newImag)
    
    def  __sub__(self, other):
        newReal=self.real-other.real
        newImag=self.imag-other.imag
        return Complex(newReal,newImag)


num1=Complex(2,3)
num2=Complex(4,5)
num1.showNumber()
num2.showNumber()
num4=Complex(7,4)
num4=num1-num2
num4.showNumber()
num3=num1+num2
num3.showNumber()
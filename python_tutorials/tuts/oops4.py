class si:
    def __init__(self,p,r,t):
        self.p=p
        self.r=r
        self.t=t
    def calc(self):
        self.Si=self.p*self.r*self.t/100
        return self.Si
    def display(self):
        print("principal=",self.p)
        print("rate=",self.r)
        print("time=",self.t)
        print("simple interest=",self.calc())
p=float(input("enter principal="))
r=float(input("enter rate="))
t=float(input("enter time="))
s=si(p,r,t)
s.display()
s.calc()


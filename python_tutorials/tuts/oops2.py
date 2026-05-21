class St:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)

s1=St("nivin",21)
s1.display()
print(s1.name,s1.age,s1.age+1)
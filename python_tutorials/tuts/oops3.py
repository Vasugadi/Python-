class Ar:
    name="nivin"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("name:",self.name)
        print("age:",self.age)

a1=Ar("nivin",21)
a1.display()
Ar.name="nivin"
a1.display()
print(Ar.name) #class variable
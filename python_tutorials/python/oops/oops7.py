class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

s1=Student("marco")
print(s1.name)
s1.display()
print(s1)
del s1
print(s1)
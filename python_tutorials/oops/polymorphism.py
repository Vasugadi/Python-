#when the same operator is allowed to have more than one form
#eg: + operator can be used for addition and concatenation

#method overloading--> same method name but different parameters
#method overriding--> same method name but different implementation
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __add__(self,other):
        return self.marks+other.marks
    def __str__(self):
        return f"Student name is {self.name} and marks are {self.marks}"
s1=Student("Karan",90)
s2=Student("Karanya",78)
print(s1+s2)
print(s1)
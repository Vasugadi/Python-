#
class Student:
    college_name = "cbit"
    def __init__(self,name,science,maths,hindi):
        self.name=name
        self.science=science
        self.maths=maths
        self.hindi=hindi
    def get_name(self):
        return self.name
    def average(self):
        avg=(self.science+self.maths+self.hindi)/3
        return avg

student1=Student("marco",90,80,70)
print(student1.get_name())
print(student1.average())


#
class Student:
    college_name = "cbit"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_name(self):
        return self.name
    def get_marks(self):
        sum=0
        for i in self.marks:
            sum+=i
        avg=sum/3
        return avg

student1=Student("marco",[90,80,70])
print(student1.get_name())
print(student1.get_marks())
        

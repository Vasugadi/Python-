#
class Student:

    def __init__ (self,name,marks):
        self.name=name
        self.marks=marks

    def get_Avg(self):
        sum=0
        for i in self.marks:
            sum += i
        return sum/len(self.marks)
    
    def get_ans(self):
        return self.get_Avg()
    
s1=Student("John",[10,20,30,40,50])
print(s1.get_ans())
print(s1.get_Avg())  # Output: 30.0
    

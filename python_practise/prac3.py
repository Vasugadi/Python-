class Student:
    college_name="Abc College"
    
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
    
    def get_Avg(self,marks):
        return sum(self.marks)/len(self.marks)
        # sum=0
        # for i in marks:
        #     sum+=i
        # return sum/len(marks)
        
    def showMarks(self):
        print(f"Name: {self.name}, College: {self.college_name}, Marks: {self.marks}")

s1=Student("John Doe",[90,80,70,60])
s1.showMarks()  # Output: Name: John Doe, College: Abc College, Marks: [90, 80, 70, 60]
avg=s1.get_Avg(s1.marks)
print("Average Marks: ",avg)  # Output: Average Marks:  75.
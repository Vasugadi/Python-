class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your avg score is:",sum/3)

s1= Student("John", [90, 85, 95])
print(s1.get_avg())
 # 90.0

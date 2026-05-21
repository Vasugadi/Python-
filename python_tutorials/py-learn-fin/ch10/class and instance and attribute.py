#class.attr same for all instances
#obj.attr different for each instance
#if the value is different for each instance, then it should be an instance attribute written by self.----
#if the value is same for all instances, then it should be a class attribute written by class.----

class Student:
    college_name="abc_college"
    name="anonymous"#class attribute
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    
s1=Student("abc",1)
print(s1.name,s1.roll_no,Student.college_name)
s2=Student("xyz",2)



#precedence of instance attribute is more than class attribute
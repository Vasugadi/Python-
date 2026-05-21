#class.attr
#obj.attr
class Student:
    college = "ABC University"  # Class variable shared by all instances

    def __init__(self, name):
        self.name = name

s2 = Student("Alice")
print(s2.name)      # Output: Alice
print(Student.college)  # Output: ABC University 

  
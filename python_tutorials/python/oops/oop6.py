#
class Student:
    college_name = "ABC"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_name(self):
        print(f"welcome{self.name}")

    def get_marks(self):
        print(f"your marks are {self.marks}")


student1 = Student("marco", 20)
student1.get_name()
student1.get_marks()
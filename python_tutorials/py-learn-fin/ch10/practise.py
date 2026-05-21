class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        return sum(self.marks) / len(self.marks)

s1= Student("John", [90, 85, 95])
print(s1.get_avg()) # 90.0

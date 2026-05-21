#method
# methods are functions that belong to objects

# creating class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    

# creating object
student1 = Student("John", 20)
student2 = Student("Jane", 22)

# calling methods
print(student1.get_name())
print(student1.get_age())
print(student2.get_name())
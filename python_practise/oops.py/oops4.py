
# methods for oops
class Student:
    college = "ABC University"  # Class variable shared by all instances

    def __init__(self, name):
        self.name=name
    
    def greet(self):
        print(f"Hello {self.name} from {self.college}")

    def welcome(self):
        print(f"Welcome {self.name} to {self.college}")

    def get_college(self):
        return self.college
    


s3=Student("bob")
print(Student.college)  # Output: ABC University

print(s3.name)  # Output: bob

s3.greet()  # Output: ABC University

s3.welcome()  # Output: Welcome bob to ABC University
print(s3.get_college())  # Output: ABC University
class Employee:
    company = "TechCorp"

    def __init__ (self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(f"Role: {self.role}, Department: {self.department}, Salary: {self.salary}")

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT",50000)

e1 = Engineer("John",25)
e1.showDetails()

e2 = Employee("Manager","HR",60000)
e2.showDetails()
# Output: Object John is being deleted
# This will raise an error since d1 is deleted
    
class Employee:
    def __init__(self, role,dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        
    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age=age
        super().__init__("accont", "finance", "50000")
        


emp = Employee("accont", "finance", "50000")
emp.showDetails()


emp.showDetails()

eng = Engineer("Raj", 30)
eng.showDetails()   
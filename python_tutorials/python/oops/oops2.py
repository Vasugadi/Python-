# constructor is a special method that is automatically called when an object is created
# it is used to initialize the object's attributes
# it is defined using the __init__ method
# it takes self as the first parameter, which represents the object itself
# it can take additional parameters to initialize the object's attributes
# it can also return None
# it is called automatically when an object is created
# it is used to initialize the object's attributes

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Salary: ", self.salary)

    def update_salary(self, increment):
        self.salary += increment

# creating objects
emp1 = Employee("John", 30, 50000)
emp2 = Employee("Jane", 25, 60000)

# calling methods   
emp1.display()
emp2.display()

# updating salary
emp1.update_salary(5000)
emp2.update_salary(7000)
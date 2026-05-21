class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius # pie r square

    def circumference(self):
        return 2*3.14*self.radius #2 pie r

c1=Circle(5)
print(c1.area())
print(c1.circumference())


class Employee:
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def info(self):
        print(f"Name is {self.name} and salary is {self.salary} and role is {self.role}")
class Engineer(Employee):
    def __init__(self,name):
        self.name=name
        super().__init__(name,1000,"developer")
        super().info()
e1=Employee("marco",1000,"developer")
e1.info()
e2=Engineer("marco")
e2.info()


class Items:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price>ord2.price
        
ord1=Items("pen",10)
ord2=Items("book",20)
print(ord1>ord2)


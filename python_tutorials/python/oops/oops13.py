class Person:
    name="anonymous"

    def changeName(self,name):
        # self.name=name# to change this
        # Person.name=name# to change this
        self.__class__.name="hero"

p1=Person()
p1.changeName("marco")
print(p1.name)
print(Person.name)

# another way by using class method
# a class method is bound to the class and receives the class as an implicit forst argument
#non-- static method cant access or modify class state and generally for utility

class Student:
    name="Anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name=name
p1=Student()
p1.changeName("rahul")
print(p1.name)
print(Student .name)
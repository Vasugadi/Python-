#class method

class Person:
    name="Anonymous"  # Class variable

    def change_name(self,name):
        self.name = name
        #self.__class__.name = name  # Change class variable using self.__class__
        #1 thing is Person.name = name  # Change class variable
    
p1=Person()
p1.change_name("John")
print(p1.name)  # Output: John
print(Person.name)  # Output: John


class Pearson:
    name = "Anonymous"  # Class variable

    @classmethod
    def change_name(cls, name):
        cls.name = name  # Change class variable using cls

p2 = Pearson()
p2.change_name("John")
print(p2.name)  # Output: John
print(Pearson.name)  # Output: John
 
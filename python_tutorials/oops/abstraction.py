#del keyword is used to delete objects in Python. It can be used to delete variables, list items, dictionary entries, or even entire objects. When you use del on an object, it removes the reference to that object from the current namespace. If there are no more references to the object, it becomes eligible for garbage collection.

#deletion of object: del s1
#deletion of attribute: del s1.marks
class Student:
    def __init__(self,fullname,marks):
        self.marks=marks
        self.name=fullname
#static method method is not bound to class or object
#it is bound to the namespace of the class
#these dont use the self parameter (works at class level)

    @staticmethod
    def greet():
        print("Hello")
s1=Student("Karan",90)

s2=Student("Karanya",78)
print(s1.__dict__) #to see the attributes of the object
del s1.marks
print(s2.__dict__)
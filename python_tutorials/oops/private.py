#private we cant access from outside the class
class Student:
    def __init__(Self,fullname,marks):
        Self.__marks=marks#to make private add __ before attribute
        Self.name=fullname

    def __get_marks(self):#private method
        return self.__marks
    
    def marks_info(self):
        return self.__get_marks()

    def set_marks(self,marks):
        self.__marks=marks
    def __hello(self):
        print("Hello")
    def welcome(self):
        self.__hello()

s1=Student("Karan",90)
#print(s1.get_marks())
s1.set_marks(95)
print(s1.marks_info())
s1.welcome()

s2=Student("Karanya",78)

#  _ _gives private access

class Person:
    __name="marco"
    def __hello(self):
        print("hello")
    def welcome(self):
        self.__hello()
        print(Person.__name)
    

p1=Person()
p1.welcome()

#p1.__hello() #this will give error as __hello is private method

#print(Person.__name) #this will give error as __name is private variable


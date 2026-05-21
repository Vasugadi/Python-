class Pr:
    def __init__(self,name):
        self.__name=name
    def __hello(self):
        print("hello")
    def hello(self):
        print("hello")
        self.__hello()
p1=Pr("pr")
p1.hello()
p1.__hello()
class Person:
    name="anonymous"
    def changename(self,name):
        #self.__class__.name=name 
        self.name=name
        #other wise Person.name=name
    @classmethod
    def changenamee(cls,name):
        cls.name=name
p1=Person()
p1.changename("Karan")
print(p1.name)
p1.changenamee("Karanya")

print(Person.name)


"""_summary
static method----> no self or cls(no class or instance attributes)
class method----> cls(class attributes)
instance method----> self(instance attributes)
"""
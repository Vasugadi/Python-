class Animal:
    def speaks(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"
class Cat(Animal):
    def speak(self):
        return "Cat meows"
    
d1=Dog()
c1=Cat()

print(d1.speak())
print(c1.speak())
print(d1.speaks())
print(c1.speaks())
print(issubclass(Dog,Animal))
print(issubclass(Cat,Animal))
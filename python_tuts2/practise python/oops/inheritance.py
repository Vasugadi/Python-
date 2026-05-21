"""
parent class and child class

types
1. single inheritance
2. multilevel inheritance
3. hierarchical inheritance-- 
4. multiple inheritance- its combination of multiple classes
5. hybrid inheritance- its combination of multiple and multilevel inheritance
"""

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
        
class Cat(Animal):
    def meow(self):
        print("Cat meows")

dog = Dog()
dog.speak()
dog.bark()

cat = Cat()
cat.speak()
cat.meow()



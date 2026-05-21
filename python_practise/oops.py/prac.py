class Circle:
    def __init__ (self,radius):
        self.radius = radius

    def area(self):
        print("Area of circle is", 3.14 * self.radius **2)

    def circumference(self):
        print("Circumference of circle is", 2 * 3.14 * self.radius)

c1=Circle(4)
c1.area()
c1.circumference()  # Output: Area of circle is 50.24


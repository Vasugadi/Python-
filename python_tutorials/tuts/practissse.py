class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


# Create a Circle object with radius 5
circle = Circle(5)

# Print the area and circumference of the circle
print("Area:", circle.area())
print("Circumference:", circle.circumference())

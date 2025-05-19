import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle with radius {self.radius:.2f} has: \nArea of circle is {self.area():.2f} \nCircumference of circle is {self.circumference():.2f}"

circle = Circle(4)
print(circle)

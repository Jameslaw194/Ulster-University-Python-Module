import math

class Shape:
    __count = 0

    def __init__(self, length):
        self._length = length
        self._area = 0
        self._boundary = 0
        Shape.__count += 1

    def calculate_area(self):
       pass

    def calculate_boundary(self):
       pass

    @classmethod
    def get_count(cls):
        return Shape.__count

    def __str__(self):
        return f"Area: {self._area:.2f}\nBoundary: {self._boundary:.2f}"


class Square(Shape):
    __count_square = 0
    def __init__(self, length):
        super().__init__(length)
        Square.__count_square += 1

    def calculate_area(self):
        return self._length * self._length

    def calculate_boundary(self):
        return self._length * 4

    @classmethod
    def get_count(cls):
        return Square.__count_square

    def __str__(self):
        return f"Area: {self.calculate_area():.2f}\nBoundary: {self.calculate_boundary():.2f}"


class Triangle(Shape):
    __count_triangle = 0
    def __init__(self, length):
        super().__init__(length)
        Triangle.__count_triangle += 1

    def calculate_area(self):
        return 0.5 * (self._length * self._length)

    def calculate_boundary(self):
        return self._length * 3

    @classmethod
    def get_count(cls):
        return Triangle.__count_triangle

    def __str__(self):
        return f"Area: {self.calculate_area():.2f}\nBoundary: {self.calculate_boundary():.2f}"


class Circle(Shape):
    __count_circle = 0
    def __init__(self, length):
        super().__init__(length)
        Circle.__count_circle += 1

    def calculate_area(self):
        return math.pi * (self._length * self._length)

    def calculate_boundary(self):
        return 2 * math.pi * self._length

    @classmethod
    def get_count(cls):
        return Circle.__count_circle

    def __str__(self):
        return f"Area: {self.calculate_area():.2f}\nBoundary: {self.calculate_boundary():.2f}"

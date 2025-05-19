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
        self.calculate_area()
        self.calculate_boundary()
        Square.__count_square += 1

    def calculate_area(self):
        self._area = self._length ** 2

    def calculate_boundary(self):
        self._boundary = 4 * self._length

    @classmethod
    def get_count(cls):
        return Square.__count_square

    def __str__(self):
        suffix = super().__str__()
        return "Square Details\n" + suffix


class Triangle(Shape):
    __countTriangle = 0

    def __init__(self, length):
        super().__init__(length)
        self.calculate_area()
        self.calculate_boundary()
        Triangle.__countTriangle += 1

    def __str__(self):
        suffix = super().__str__()
        return "Triangle Details\n"+ suffix

    def calculate_area(self):
        self._area = 0.5 * self._length * self._length


    def calculate_boundary(self):
        self._boundary = (2 * self._length) + math.sqrt(2 * self._length * self._length)


    @classmethod
    def get_count(cls):
        return Triangle.__countTriangle


class Circle(Shape):
    __countCircle = 0

    def __init__(self, length):
        super().__init__(length)
        self.calculate_area()
        self.calculate_boundary()
        Circle.__countCircle += 1

    def __str__(self):
        suffix = super().__str__()
        return "Circle Details\n" + suffix

    def calculate_area(self):
        self._area = (self._length * self._length) * math.pi


    def calculate_boundary(self):
        self._boundary = (2 * self._length) * math.pi


    @classmethod
    def get_count(cls):
        return Circle.__countCircle



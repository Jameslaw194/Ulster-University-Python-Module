from Shapes import *


def main():
    dimension = float(input("Enter dimension: "))
    triangle1 = Triangle(dimension)

    print("The number of shapes created:", Shape.get_count())
    print("The number of triangles created:", Triangle.get_count())

    print(triangle1)


main()

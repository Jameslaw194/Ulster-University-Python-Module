from Shapes import *


def main():

    dimension = float(input("Enter dimension: "))
    circle1 = Circle(dimension)

    print("The number of shapes created:", Shape.get_count())
    print("The number of circles created:", Circle.get_count())
    print(circle1)


main()

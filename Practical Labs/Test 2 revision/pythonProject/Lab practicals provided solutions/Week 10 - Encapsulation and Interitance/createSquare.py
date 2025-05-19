from Shapes import *


def main():
    dimension = float(input("Enter dimension: "))
    square1 = Square(dimension)

    print("The number of shapes created:", Shape.get_count())
    print("The number of squares created:", Square.get_count())
    print(square1)


main()

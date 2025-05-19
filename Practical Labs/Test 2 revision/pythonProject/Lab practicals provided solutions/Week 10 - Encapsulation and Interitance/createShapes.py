from Shapes import *


def main():
    choice = 'y'

    while choice == 'y':

        print("Enter 1 for Square, 2 for Triangle, 3 for Circle:")
        userChoice = int(input("Enter choice: "))
        dimension = float(input("Enter dimension: "))

        if userChoice == 1:
            s1 = Square(dimension)
            print(s1)

        elif userChoice == 2:
            s1 = Triangle(dimension)
            print(s1)

        else:
            s1 = Circle(dimension)
            print(s1)

        print("")
        choice = input("Do you want to go again? ('y' for yes): ")
        print("")

    print("The number of shapes created:", Shape.get_count())
    print("The number of squares created:", Square.get_count())
    print("The number of triangles created:", Triangle.get_count())
    print("The number of circles created:", Circle.get_count())

main()

import Shapes
again = 'y'

def main():
    shapeChoice = int(input("Enter the shape you want to calculate.\n1. Square\n2. Triangle\n3. Circle\n"))

    if shapeChoice == 1:
        shapeLength = int(input("Enter the length of one side: "))
        print(Shapes.Square(shapeLength))

    if shapeChoice == 2:
        shapeLength = int(input("Enter the length of one side: "))
        print(Shapes.Triangle(shapeLength))

    if shapeChoice == 3:
        shapeLength = int(input("Enter the length of the radius: "))
        print(Shapes.Circle(shapeLength))


while again == 'y' or again == 'Y':
    again = input("Would you like to calculate another shape? (y/n)")
    if again == 'y' or again == 'Y':
        main()
    if again == 'n' or again == 'N':
        print("The number of shapes created: ", Shapes.Shape.get_count())
        print("The number of squares created: ", Shapes.Square.get_count())
        print("The number of triangles created: ", Shapes.Triangle.get_count())
        print("The number of circles created: ", Shapes.Circle.get_count())
        break
    else:
        print("Bad input, please try again.")

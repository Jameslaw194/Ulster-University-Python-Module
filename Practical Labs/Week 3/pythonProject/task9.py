# this program draws a square of side 100
# draw a line of length 100
# then turn left thru 90 degrees
# repeat this process 4 times to
# draw the four sides of the square
#import turtle
import turtle
import time
sideLength = int(input("Enter the side length: "))
penThickness = int(input("Enter the pen thickness: "))
animationSpeed = int(input("Enter the animation speed: "))
penColour = input("Enter the pen colour: ")

turtle.pensize(penThickness)
turtle.speed(animationSpeed)
turtle.color(penColour)

turtle.forward(sideLength)
turtle.left(90)
turtle.forward(sideLength)
turtle.left(90)
turtle.forward(sideLength)
turtle.left(90)
turtle.forward(sideLength)
turtle.left(90)

time.sleep(10)
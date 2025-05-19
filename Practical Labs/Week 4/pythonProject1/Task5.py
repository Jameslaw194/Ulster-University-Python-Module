
# this program draws a square of side 100

#import turtle
import turtle

sides = int(input("Enter how many sides of the shape you want: "))

turnAngle = 360/sides
# draw a line of length 100
# then turn left thru 90 degrees
# repeat this process 4 times to
# draw the four sides of the square

for i in range(sides):
    turtle.forward(100)
    turtle.left(turnAngle)
#end of for loop

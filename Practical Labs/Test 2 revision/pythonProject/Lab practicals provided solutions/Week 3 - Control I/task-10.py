# this program draws a square of side side

#import turtle
import turtle

colour = input('What pen colour do you want to use?')
thick = int(input('How thick should the pen be?'))
speed = int(input('How fast do you wnat the turtle to draw?'))
side = int(input('How big should the square be?'))

turtle.pencolor(colour)
turtle.pensize(thick)
turtle.speed(speed)

            
# draw a line of length 100
# then turn left thru 90 degrees
# repeat this process 4 times to
# draw the four sides of the square

for x in range(4):
    turtle.forward(side)
    turtle.left(90)


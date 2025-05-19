
#com101 week 4 lab task 5
# modifications to code noted with triple #
### this program draws a polygon of side 100

#import turtle
import turtle

### request input on the number of sides
sides = int(input('How many sides do you wnat your polygon to have?'))

###modify number of loops and angle turned thru
for i in range(sides):
    turtle.forward(100)
    turtle.left(360/sides)
#end of for loop

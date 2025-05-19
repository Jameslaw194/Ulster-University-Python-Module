# this program draws 36 squares of side 100
# it also goes a little further than the question in the lab question
#by adding colour

#import turtle
import turtle
turtle.hideturtle()
turtle.speed(0)
turtle.colormode(255)  ####otherwise rgb entries are rejected

for j in range(36):
    turtle.setheading(j*10)

    turtle.fillcolor((j*5,1,200)) ##extra
    turtle.begin_fill()          ##extra
#draw single square with heading j*10
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill() ###extra
#end of i for loop
#end of j for loop        


    

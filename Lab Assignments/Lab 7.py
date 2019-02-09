x = int(input("What is the x-coordinate? "))
y = int(input("What is the y-coordinate? "))
s = int(input("What is the length of each square? "))

import turtle
turtle.speed("fastest")
turtle.penup()
turtle.goto(x,y)
def turtlesquare(c):
    turtle.showturtle()
    turtle.pendown()
    turtle.color(c)
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(s)
    for i in range (3):
        turtle.right(90)
        turtle.forward(s)
    turtle.end_fill()
    turtle.penup()
    turtle.right(90)
    turtle.forward(s*2)
    turtle.right(90)

for n in range(1,5):
    for i in range (1,5):
        turtlesquare("black")
    
    turtle.right(90)
    turtle.forward(s*7)
    turtle.left(90)
    
    for i in range(1,5):
        turtlesquare("yellow")
        
    turtle.right(90)
    turtle.forward(s*9)
    turtle.left(90)
    turtle.forward(s*2)

turtle.goto(x+s,y)

for n in range(1,5):
    for i in range (1,5):
        turtlesquare("yellow")
    
    turtle.right(90)
    turtle.forward(s*7)
    turtle.left(90)
    
    for i in range(1,5):
        turtlesquare("black")
        
    turtle.right(90)
    turtle.forward(s*9)
    turtle.left(90)
    turtle.forward(s*2)
    
turtle.goto(x+s*10,y)

for n in range(1,5):
    for i in range (1,5):
        turtlesquare("black")
    
    turtle.right(90)
    turtle.forward(s*7)
    turtle.left(90)
    
    for i in range(1,5):
        turtlesquare("yellow")
        
    turtle.right(90)
    turtle.forward(s*9)
    turtle.left(90)
    turtle.forward(s*2)

turtle.goto(x+s*11,y)

for n in range(1,5):
    for i in range (1,5):
        turtlesquare("yellow")
    
    turtle.right(90)
    turtle.forward(s*7)
    turtle.left(90)
    
    for i in range(1,5):
        turtlesquare("black")
        
    turtle.right(90)
    turtle.forward(s*9)
    turtle.left(90)
    turtle.forward(s*2)

input()
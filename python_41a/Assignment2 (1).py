#Syuta Sugawara


"""

Divide the drawing screen into quadrants.
In the middle of each quadrant, draw one of these shapes:  circle,
rectangle, triangle, polygon in different colors.

"""

import turtle

t=turtle.Turtle()
t.penup()
t.setpos(0,300)
t.pendown()
t.setpos(0,-300)
t.penup()
t.setpos(-300,0)
t.pendown()
t.setpos(300, 0)
t.penup()
t.setpos(-150,100)
t.pendown()
t.pencolor("red")
t.circle(50)

t.penup()
t.goto(100,175)
t.color("blue")
t.pendown()
t.goto(200,175)
t.goto(200,175)
t.goto(200,125)
t.goto(100,125)
t.goto(100,175)

t.penup()
t.goto(150,-125)
t.pendown()
t.color("green")
t.right(60)
t.fd(100)
t.right(120)
t.fd(100)
t.right(120)
t.fd(100)
t.right(60)

t.penup()
t.goto(-150, -200)
t.pendown()
t.color("black") 
n=int(input("How many ?:"))
length =int(input("Enter the lengh:"))
angle = 360.0 / n
for i in range(n):
   t.left(angle)
   t.fd(length)
   





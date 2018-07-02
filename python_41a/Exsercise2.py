"""
Using Turtle graphics,
draw a big X on the screen
using a color and width of your choice.

"""
import turtle
t=turtle.Turtle()
t.color("blue")
t.pensize(10)
t.penup()
t.goto(-500,500)
t.pendown()
t.goto(500,-500)
t.penup()
t.goto(500,500)
t.pendown()
t.goto(-500,-500)

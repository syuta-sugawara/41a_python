#Syuta Sugawara

"""
Write a function that takes a random integer between 1 and 6.
Use the random integer in the function to conditionally draw 1 to 6 sided dice.
For example, a random integer of 2 should draw a dice with 2 dots on it,
and a random integer of 5 should draw a dice with 5 dots on it.

You can make a 2D or 3D dice representation.
"""
import turtle
import random

t=turtle.Turtle()
t.color("black","black")
t.speed(0)


def draw_square():
   t.penup()
   t.setpos(-250,250)
   t.pendown()
   t.goto(250,250)
   t.goto(250,-250)
   t.goto(-250,-250)
   t.setpos(-250,250)
draw_square()

def fill_dots():
   t.pendown()
   t.begin_fill()
   t.circle(50)
   t.end_fill()
   

def draw_circle():
   dots=random.randint(1,6)
   
   if dots==1:
       t.penup()
       t.goto(0,-50)
       fill_dots()
   if dots==2:
       t.penup()
       t.goto(-125,75)
       fill_dots()
       t.penup()
       t.goto(125,-175)
       fill_dots()
       
   if dots==3:
      t.penup()
      t.goto(-125,75)
      fill_dots()
      t.penup()
      t.goto(0,-50)
      fill_dots()
      t.penup()
      t.goto(125,-175)
      fill_dots() 

   if dots==4:
      t.penup()
      t.goto(-125,75)
      fill_dots()
      t.penup()
      t.goto(125,-175)
      fill_dots()
      t.penup()
      t.goto(-125,-175)
      fill_dots()
      t.penup()
      t.goto(125,75)
      fill_dots()
      
   if dots==5:
      t.penup()
      t.goto(0,-50)
      fill_dots()
      t.penup()
      t.goto(-125,75)
      fill_dots()
      t.penup()
      t.goto(125,-175)
      fill_dots()
      t.penup()
      t.goto(-125,-175)
      fill_dots()
      t.penup()
      t.goto(125,75)
      fill_dots()

   if dots==6:
      t.penup()
      t.goto(-125,110)
      fill_dots()
      t.penup()
      t.goto(-125,-50)
      fill_dots()
      t.penup()
      t.goto(-125,-210)
      fill_dots()
      t.penup()
      t.goto(125,110)
      fill_dots()
      t.penup()
      t.goto(125,-50)
      fill_dots()
      t.penup()
      t.goto(125,-210)
      fill_dots()

draw_circle()
   

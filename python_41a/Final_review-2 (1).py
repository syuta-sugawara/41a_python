"""
1. Convert this function to use a Map:

  def MapIt(nlist):
        alist = []
        for n in nlist:
              alist.insert( len(alist), SquareIt(n) )
              # SquareIt multiplies n*n
        return alist
   
2. Using Python regular expressions, write the statements
to find all the numbers in a line of text.
Example:  "De Anza College, 21250 Stevens Creek Blvd., Cupertino, 95014"
 
3. Write a function using Tkinter to draw a triangle given 3 points:
   Left, Mid, Right.
Assume TKinter has been initialized.
Also, draw the same triangle using Turtle.
"""

#1,Answer
def SquareIt(n):
   return n*n
nlist=[1,2,3,4,5]
alist=list(map(SquareIt ,nlist))
print(alist)

#2,Answer
import re
li=re.findall(r"\d","De Anza College, 21250 Stevens Creek Blvd., Cupertino, 95014")
print(li)

#3,Answer
# I wrote equilateral triangle

from tkinter import *
root=Tk()

c = Canvas(root,width=500,height=500,bg='yellow')
c.create_polygon((10, 110, 60, 10, 110, 110), fill="red")
c.pack()
def quit():
    global root
    root.quit()
Button(root, text="Quit", command=quit).pack()

mainloop()


import turtle
t = turtle.Turtle()
t.penup()
t.goto(10,110)
t.pendown()
t.goto(60,10)
t.goto(110,110)
t.goto(10,110)
turtle.done()


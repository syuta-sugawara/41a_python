from tkinter  import *

root=Tk()
root.geometry("800x800") 
canvas=Canvas(root,bg="blue",width=800, height=800)
canvas.grid()

a = None
b = None

def Click(event):
   global a
   global b

   if a is None:
      a = event.x
      b = event.y
      
   x = event.x
   y = event.y
   r = 50
   canvas.create_oval(x - r, y - r, x + r, y + r, fill="gray",width=5)
   canvas.create_line(a, b, x, y)
   a = x
   b = y

   
canvas.bind("<Button-1>",Click)


canvas.pack()

root.mainloop()


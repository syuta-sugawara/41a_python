import csv
import re
from tkinter import *

class ManageFile():
    def __init__(self):
        self.li=[]

    def Open_File(self,file):
        self.file=open(file)
        self.csv=csv.reader(self.file)

    def Read_File(self):
        for line in self.csv:
            self.li.append(line)

    def Close_File(self):
        self.file.close()

    def Output(self):
        for line in range(0,len(self.li)):
            print(self.li[line])

    def __str__(self):
        return str(self.li)

    def __iter__(self):
        return iter(self.li)


    def Remove_Parenthesis(self):
        temp=[]

        for line in range(0,len(self.li)):
            temp.append([])
            a=re.sub(r'\(|\)',"",str(self.li[line][0]))
            b=re.sub(r'\(|\)', "",str(self.li[line][1]))
            temp[line].append(a)
            temp[line].append(b)
        print(temp)
        return temp

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_x(self,x):
        self.x=x

    def set_y(self,y):
        self.y=y

class Manages_Cartesian():
    def __init__(self,li):

        self.li = []

        for line in range(0, len(li)):
            p = Point(li[line][0], li[line][1])
            self.li.append(p)

        self.max_x = self.li[0].get_x()
        self.min_x = self.li[0].get_x()
        self.max_y = self.li[0].get_y()
        self.min_y = self.li[0].get_y()

        for point in self.li:
            if self.max_x < point.get_x():
                self.max_x = point.get_x()

            if self.min_x > point.get_x():
                self.min_x = point.get_x()

            if self.max_y < point.get_y():
                self.max_y = point.get_y()

            if self.min_y > point.get_y():
                self.min_y = point.get_y()

            self.number = len(self.li)

    def __iter__(self):
        return iter(self.li)

    def numberOfItem(self):
        return self.number

    def Output(self):
        print(str(self.max_x),
              str(self.min_x),
              str(self.max_y),
              str(self.min_y),
              str(self.number))



class draw_bytkinter():
    def __init__(self,right,height,x_max,x_min,y_max,y_min,li):
        self.li=li
        self.width= right
        self.height=height
        self.xrange = float(x_max) - float(x_min)
        self.yrange = float(y_max) - float(y_min)

    def __str__(self):
        return str(self.li)

    def __iter__(self):
        return iter(self.li)

    def Draws(self):

        window = Tk()
        canvas = Canvas(window)

        canvas.config(width=self.width, height=self.height)

        canvas.pack()

        scale_x = self.width / (self.xrange  + 1)
        scale_y = self.height / (self.yrange + 1)

        origin_x = self.width  / 2
        origin_y = self.height  / 2
        nega_width = 0 - self.width
        nega_height = 0 - self.height

        canvas.create_line(nega_width, origin_y, self.width , origin_y)
        canvas.create_line(origin_x, nega_height, origin_x, self.height)


        last_x = None

        for point in self.li:
            x = origin_x + scale_x * float(point.get_x())
            y = origin_y - scale_y * float(point.get_y())
            r = 2
            if last_x is None:
                last_x = x
                last_y = y

            canvas.create_oval(x - r, y - r, x + r, y + r)
            canvas.create_line(last_x, last_y, x, y)
            last_x = x
            last_y = y
        window.mainloop()



class draw_bymatplot():
    def __init__(self):

        x=[]
        y=[]
        for line in range(0,len(li)):
            x.append(li[line][0])
            y.append(li[line][1])

        self.xlist=x
        self.ylist=y

    def Draw_line(self):
        plt.plot(self.xlist,self.ylist)
        plt.show()


x=ManageFile()
file=input("choose file")
x.Open_File(file)
x.Read_File()
x.Close_File()
temp_li=x.Remove_Parenthesis()
x=Manages_Cartesian(temp_li)

#graph_var=draw_bymatplot(temp_li)
#graph_var.Draw_line()
draw=draw_bytkinter(800,800,x.max_x,x.min_x,x.max_y,x.min_y,x.li)
print(draw)
draw.Draws()

coordinate=Manages_Cartesian(temp_li)
number=coordinate.numberOfItem()
print(number)
coordinate.Output()

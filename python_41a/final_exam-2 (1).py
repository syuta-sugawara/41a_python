#class Read():
#    def __init
import csv
import re

class Book():
    def __init__(self,idnum,isbn,title,name,year,ty,pages,price):
        self.idnum=idnum
        self.isbn=isbn
        self.title=title
        self.name=name
        self.year=year
        self.type=ty
        self.pages=pages
        self.price=price

    def __str__(self):
        return str(self.idnum)+","+str(self.isbn)+","+str(self.title)+","+str(self.name)+","+str(self.year)+","+str(self.type)+","+str(self.pages)+","+str(self.price)

class CD():
    def __init__(self,idnum,isbn,title,year,first,last,price):
        self.idnum =idnum
        self.isbn =isbn
        self.title=title
        self.year=year
        self.first=first
        self.last =last
        self.price=price

    def __str__(self):
        return str(self.idnum)+","+str(self.isbn)+","+str(self.title)+","+str(self.year)+","+str(self.first)+","+str(self.last)+","+str(self.price)
    
class BookLibrary():
    def __init__(self):
      self.library=[]

    def Read_file(self):
      import csv
      import re
      pattern=r"4.+"
      temp=[]
      with open('Inventory.csv') as f:
         for line in csv.reader(f):
    
            obj1=re.match(pattern,line[0])
            
            if obj1:
                temp.append(line)
    
      for line in range(0,len(temp)):
          bk=Book(temp[line][0],temp[line][1],
                temp[line][2],temp[line][3],
                temp[line][4],temp[line][5],
                temp[line][6],temp[line][7])
      self.library.append(bk)

    def __len__(self):
        return len(self.library)

    def Output(self):
        for line in self.library:
            print(line)



class CDLibrary():
    def __init__(self):
      self.library=[]

    def Read_file(self):
      import csv
      import re
      pattern=r"7.+"
      temp=[]
      with open('Inventory.csv') as f:
         for line in csv.reader(f):
    
            obj1=re.match(pattern,line[0])
            
            if obj1:
                temp.append(line)
      
      for line in range(0,len(temp)):
          cd=CD(temp[line][0],temp[line][1],
                temp[line][2],temp[line][3],
                temp[line][4],temp[line][5],
                temp[line][6])
      self.library.append(cd)

    def __len__(self):
        return len(self.library)

    def Output(self):
        for line in self.library:
            print(line)



x=CDLibrary()
x.Read_file()

y=BookLibrary()
y.Read_file()

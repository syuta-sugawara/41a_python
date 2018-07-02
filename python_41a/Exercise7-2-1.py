
class Person:
   def __init__(self,give_name,family_name):
      self.first_name=give_name
      self.last_name=family_name
   def __str__(self):
      return  "first name is "+self.first_name+" last name is "+self.last_name

class Passenger(Person):
   def __init__(self,give_name,family_name,row_num,seat_num):
      super().__init__(give_name,family_name)
      self.row=row_num
      self.seat=seat_num
   
      
   def __str__(self):
      return "first name is "+self.first_name+", last name is "+self.last_name+", row number "+self.row+", seat number "+self.seat

def readfile():
      row=[]
      file=open("Passenger.csv")
      for i in file:
         row.append(i.split(","))
      file.close()

      jet=[]
      for num in range(len(row)):
         
         x=Passenger(row[num-1][0],row[num-1][1],row[num-1][2],row[num-1][3])
         jet.append(x)

      return jet

def show_jet(jet):
      for passenger in jet:
         print(passenger)

def main():  
   result=readfile()
   show_jet(result)

main()
   

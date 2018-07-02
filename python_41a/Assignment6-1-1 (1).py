#Syuta Sugawara
#Assignment6

class Capital:
   def __init__(self,a):
      li=[]
      file=open("StateCapitols-1.csv")
      for line in file:
          li.append(line.split(","))
          
      self.capital=a

      for i in range(len(li)):

         if a==li[i][1]:
            self.state=li[i][0]
            self.latitude=li[i][2]
            self.longitude=li[i][3]
         
   def __str__(self):
      return "state :"+self.state+"\ncapital :"+self.capital+"\nlatitude :"+self.latitude+"\nlongitude :"+self.longitude

   def __add__(self,other):
      import math
      radius= 6371000 
      dLat = math.radians( float(other.latitude)-float(self.latitude) )
      dLong = math.radians( float(other.longitude)-float(self.longitude) )
      nA = math.pow(math.sin(dLat/2.0),2.0) + math.cos( math.radians(float(self.latitude))) * math.cos(math.radians(float(other.latitude))) * math.pow(math.sin(dLong/2.0),2.0)
      nC = 2.0 * math.atan2( math.sqrt(nA), math.sqrt( 1.0 - nA ))
      distance = radius * nC
      km=distance/1000
      return "distance between these two points is equal to %f km " % km

   def Haversine(self,other):
      import math
      radius= 6371000 
      dLat = math.radians( float(other.latitude)-float(self.latitude) )
      dLong = math.radians( float(other.longitude)-float(self.longitude) )
      nA = math.pow(math.sin(dLat/2.0),2.0) + math.cos( math.radians(float(self.latitude))) * math.cos(math.radians(float(other.latitude))) * math.pow(math.sin(dLong/2.0),2.0)
      nC = 2.0 * math.atan2( math.sqrt(nA), math.sqrt( 1.0 - nA ))
      distance = radius * nC
      km=distance/1000
      return "distance between these two points is equal to %f km " % km

         
      
print("we can use Capital class")

capital=input("Enter state capital :")
x=Capital(capital)
print(x)

capital=input("Enter state capital :")
y=Capital(capital)
print(y)
print(x+y)
print(x.Haversine(y))

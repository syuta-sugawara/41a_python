#Syuta Sugawara
#Assignment5

"""

Here are the measurement calculations:
   number = 10 
   centimeters = 0.3937
   inches = 1 / centimeters
   feet = 12
   meters = 100
   miles = 5280
   kilometers = 1000
   km = number * ( feet * miles ) / ( centimeters * meters * kilometers)
   (km*( centimeters * meters * kilometers))/( miles ) =number*feet
   miles = number * ( meters * kilometers ) / ( inches * feet * miles )

"""

class  Miles:

      def __init__(self,number):
         self.mile=number
      
      def mile_to_km(self):
            number = 10 
            centimeters = 0.3937
            inches = 1 / centimeters
            feet = 12
            meters = 100
            miles = 5280
            kilometers = 1000

            return self.mile * ( feet * miles ) / ( centimeters * meters * kilometers)

      def mile_to_meters(self):
         return self.mile/0.00062137

      def mile_to_centimeters(self):
         return self.mile*160934.4

      def mile_to_inches(self):
         return self.mile * 63360

      def mile_to_feet(self):
         return self.mile* 5280.0


miles=float(input("Enter the miles :"))
x=Miles(miles)
print("km : ",x.mile_to_km())
print("meters : ",x.mile_to_meters())
print("centimeters : ",x.mile_to_centimeters())
print("inches : ",x.mile_to_inches())
print("feet : ",x.mile_to_feet())

class  Km:

      def __init__(self,number):
         self.km=number

      def km_to_miles (self):
            number = 10 
            centimeters = 0.3937
            inches = 1 / centimeters
            feet = 12
            meters = 100
            miles = 5280
            kilometers = 1000

            return self.km * ( meters * kilometers ) / ( inches * feet * miles )

      def km_to_meters(self):
            return  self.km/0.0010000

      def km_to_centimeters(self):
            return  self.km*30.48
 
      def km_to_inches(self):
            return  self.km*39370.07874

      def km_to_feet(self):
            return  self.km*3280.84

      
km=float(input("Enter the km :"))
y=Km(km)
print("miles : ",y.km_to_miles())
print("meters : ",y.km_to_meters())
print("centimeters : ",y.km_to_centimeters())
print("inches : ",y.km_to_inches())
print("feet : ",y.km_to_feet())



class Feet:
      def __init__(self,example):
               self.feet=example

      def feet_to_meters(self):
         return self.feet/3.2808                 

      def feet_to_centimeters(self):
         return self.feet*1-30.48

      def feet_to_miles(self):
            return  self.feet*0.00018939

      def feet_to_inches(self):
            return  self.feet*12

      def feet_to_km(self):
            return  self.feet*0.0003048


example=float(input("Enter the feet :"))
z=Feet(example)
print("meters : ",z.feet_to_meters())
print("miles : ",z.feet_to_miles())
print("centimeters : ",z.feet_to_centimeters())
print("inches : ",z.feet_to_inches())
print("km : ",z.feet_to_km())


class Meters:
       def __init__(self,number):
           self.meters=number

       def meters_to_feet(self):
               return self.meters*3.2808                   

       def meters_to_inches(self):
               return self.meters*39.370                   

       def meters_to_centimeters(self):
               return self.meters/0.010000

       def meters_to_miles(self):
               return  self.meters*0.00062137

       def meters_to_km(self):
               return  self.meters/1000

        
meters=float(input("Enter the meters :"))
a=Meters(meters)
print("feet : ",a.meters_to_feet())
print("inches : ",a.meters_to_inches())
print("centimeters : ",a.meters_to_centimeters())
print("miles : ",a.meters_to_miles())
print("km : ",a.meters_to_km())


class Inches:
       def __init__(self,number):
               self.inches=number

       def inches_to_centimeters(self):
               return self.inches*2.54 

       def inches_to_feet(self):
               return self.inches*0.0833333333                  

       def inches_to_mile(self):
               return self.inches*1.57828e-5

       def inches_to_meters(self):
               return  self.inches*0.0254

       def inches_to_km(self):
               return  self.inches*2.54e-5


inches=float(input("Enter the inches :"))
b=Inches(inches)
print("centimeters : ",b.inches_to_centimeters())
print("feet : ",b.inches_to_feet())
print("mile : ",b.inches_to_mile())
print("meters : ",b.inches_to_meters())
print("km : ",b.inches_to_km())


class Centimeters:

      def __init__(self,number):
               self.centimeters=number

      def centimeters_to_inches(self):
               return self.centimeters*0.39370079                    


      def centimeters_to_feet(self):
               return self.centimeters*0.032808399                  


      def centimeters_to_mile(self):
               return self.centimeters* 0.0000062


      def centimeters_to_meters(self):
               return  self.centimeters*0.01

      def centimeters_to_km(self):
               return  self.centimeters*0.00001
      

centimeters=float(input("Enter the centimeters :"))
c=Centimeters(centimeters)
print("inches : ",c.centimeters_to_inches())
print("feet : ",c.centimeters_to_feet())
print("miles : ",c.centimeters_to_mile())
print("km : ",c.centimeters_to_km())
print("meters : ",c.centimeters_to_meters())

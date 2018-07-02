# Syuta Sugawara

"""
Write a Class called "Calculator".  The calculator has 4 functions:

* Add:  adds two numbers

* Subtract:  subtracts two numbers

* Multiply:  multiplies two numbers

* Divide:  divides two numbers

Demonstrate that your Calculator works.

"""

class Calculator:

   def __init__(self,a_num,b_num):
      self.x=a_num
      self.y=b_num
   
   def add (self):
      return self.x+self.y

   def subtracts (self):
      if self.x>=self.y:
         return self.x-self.y
      else:
         return self.y-self.x
      
   def multiply (self):
      return self.x*self.y

   def divide (self):
      return self.x/self.y

a= float(input("Enter a number x: "))
b = float(input("Enter a number y: "))
x = Calculator(a, b)
print(x.add())
print(x.subtracts())
print(x.multiply())
print(x.divide())



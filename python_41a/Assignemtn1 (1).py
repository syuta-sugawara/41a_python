#Syuta Sugawara

"""
Convert Assignment 0 to use functions by embedding
the Fahrenheit and Celsius calculations in separate functions.
Test your functions to demonstrate the work correctly.  For example:

100 degrees Celsius = 212 degrees Fahrenheit

32 degrees Fahrenheit = 0 degrees Celsius
"""

def celsius_to_fahrenheit():
   celsius=int(input("Enter the Celsius :"))
   fahrenheit =celsius*9/5+32
   print('fahrenheit is ',fahrenheit)


def fahrenheit_to_celsius():
   fahrenheit=int(input("Enter the Fahrenheit :"))
   celsius =(fahrenheit-32) /(9/5)
   print('celsius is ',celsius)


celsius_to_fahrenheit()
fahrenheit_to_celsius()


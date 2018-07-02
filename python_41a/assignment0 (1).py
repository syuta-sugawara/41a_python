
"""

Write a Python script to convert Fahrenheit to Celsius and Celsius to Fahrenheit.

Celcius Formula:  Celsius = (Fahrenheit - 32) / (9 / 5)

Fahrenheit Formula:  Fahrenheit = Celsius * 9 / 5 + 32

Prompt the user to enter a Fahrenheit / Celsius value and then perform the calculations.

"""

def fahrenheit_to_celsius():
   fahrenheit=int(input("Enter the Fahrenheit :"))
   celsius =(fahrenheit-32) /(9/5)
   print('celsius is ',celsius)

def celsius_to_fahrenheit():
   celsius=int(input("Enter the Celsius :"))
   fahrenheit =celsius*9/5+32
   print('fahrenheit is ',fahrenheit)

fahrenheit_to_celsius()
celsius_to_fahrenheit()

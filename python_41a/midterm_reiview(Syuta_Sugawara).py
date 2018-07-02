
#Python Midterm Review
#Syuta Sugawara
"""
1. 
Given an 8-bit binary string, (eg. "10101010") convert
it to decimal (base 10).  Use Python bit operations.
"""


def convert_bit_decimal(bit):
    bin_li = list(bit)
    bin_li.reverse()
    decimal_number = 0
    for x in range(0, len(bin_li)):
        decimal_number += int(bin_li[x]) << x
    return decimal_number

bit=input("Enter 8digit:")
print(convert_bit_decimal(bit))



"""
2. 
Show how to print out a list in reverse order -
example list( [1,2,3,4,5,6,7,8,9,10] ).
Do not use the list.reverse() function.
"""


li=[1,2,3,4,5,6,7,8,9,10]
print(li[::-1])
for i in li[::-1]:
   print(i)



"""
3. 
Write a function to return a MegaMillions lottery ticket:
5 numbers range from 1 to 70 and 1 number ranges from 1 to 25.

"""


def MegaMillion():

      import random
      MegaMillions=[]
      while len(MegaMillions)<=5:
            a_num=random.randint(1,70)
            if a_num not in MegaMillions:
                  MegaMillions.append(a_num)

      while len(MegaMillions)<=6:
            b_num=random.randint(1,25)
            if b_num not in MegaMillions:
                  MegaMillions.append(b_num)

      print(MegaMillions)

MegaMillion()

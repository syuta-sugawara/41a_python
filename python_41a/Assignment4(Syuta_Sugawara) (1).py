#Syuta Sugawara

import math

def ShiftsB(number):
    log10 = math.log(number+1)
    log2 = log10 / math.log(2)
    shifts = math.ceil(log2)
    return shifts


def Bitpattern(number , shifts):
      while shifts>0:
         if number & (1 << shifts-1 ) > 0:
            print(1)
         else:
            print(0)
         shifts-=1

number= int(input("Enter number: "))
shifts=ShiftsB(number)
print(shifts)
Bitpattern(number,shifts)


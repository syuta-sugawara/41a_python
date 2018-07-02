#Syuta Sugawara

"""
Create a user defined class that contains these Roman Numeral Lists:

ones = "I","II","III","IV","V","VI","VII","VIII","IX" 
tens = "X", "XX","XXX"12, "XL", "L", "LX", "LXX", "LXXX", "XC"
hundreds = "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"

The purpose of this class is to convert Decimal values to Roman Numerals.
When the user enters a number, like 123, your class should convert it to:
CXXIII

The range on the input numbers is 1 to 999.

"""
class Roman_Numeral:
      def __init__(self,three_digit):
            self.number=three_digit
            
                         
      def convert(self):

            if len(self.number)==3 and 0!=int(self.number[0]) and 0!=int(self.number[1]) and 0!=int(self.number[2]):

                        array=[]
                        array.append(int(self.number[0]))
                        array.append(int(self.number[1]))
                        array.append(int(self.number[2]))
                        a=["I","II","III","IV","V","VI","VII","VIII","IX"]
                        b=["X", "XX","XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
                        c=["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]            
                        result_number=c[array[0]-1]+b[array[1]-1]+a[array[2]-1]


            if len(self.number)==3 and 0!=int(self.number[0]) and  0!=int(self.number[1]) and 0==int(self.number[2]):

                        array=[]
                        array.append(int(self.number[0]))
                        array.append(int(self.number[1]))
                        b=["X", "XX","XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
                        c=["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]            
                        result_number=c[array[0]-1]+b[array[1]-1]


            if len(self.number)==3 and 0!=int(self.number[0]) and 0!=int(self.number[1]) and 0==int(self.number[2]):
                        array=[]
                        array.append(int(self.number[0]))
                        array.append(int(self.number[1]))
                        b=["X", "XX","XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
                        c=["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]            
                        result_number=c[array[0]-1]+b[array[1]-1]

            if len(self.number)==3 and 0!=int(self.number[0]) and 0==int(self.number[1]) and 0==int(self.number[2]):
                        array=[]
                        array.append(int(self.number[0]))
                        c=["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]            
                        result_number=c[array[0]-1]


            if len(self.number)==2 and 0!=int(self.number[0]) and 0!=int(self.number[1]):
                  
                         array=[]
                         array.append(int(self.number[0]))
                         array.append(int(self.number[1]))
                         a=["I","II","III","IV","V","VI","VII","VIII","IX"]
                         b=["X", "XX","XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
                         result_number=b[array[0]-1]+a[array[1]-1]


            
            if len(self.number)==2 and 0!=int(self.number[0]) and 0==int(self.number[1]):
                  
                         array=[]
                         array.append(int(self.number[0]))
                         b=["X", "XX","XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
                         result_number=b[array[0]-1]
            
            if len(self.number)==1:
                        array=[]
                        array.append(int(self.number[0]))
                        a=["I","II","III","IV","V","VI","VII","VIII","IX"]
                        result_number=a[array[0]-1]

            return result_number
                                                                   
digit=input("Enter digit number :")
x=Roman_Numeral(digit)
print(x.convert())
                                                        

#Version#3 midterm spring'18
#Syuta Sugawara

#Question1

filename=("MorseCode.csv")
fi=open(filename)
li=[line.split(",") for line in fi.readlines()]
fi.close()

class Morse:
   
      def __init__(self,x,y):
         self.signal=x
         self.morse=y

      def __str__(self):
         return '%s represents %s'% (self,self.morse)

      def __eq__(self,others):
            self.morse==others.morse
            return True

#Question2

   
class Morse:
   
      def __init__(self,x,y):
         self.signal=x
         self.morse=y

      def __str__(self):
         return '%s represents %s'% (self.signal,self.morse)
      
     

#This is the answer
def readfile_change_to_Morse_UDT():
      #file_read
      filename=("MorseCode.csv")
      fi=open(filename)
      li=[line.split(",") for line in fi.readlines()]

      fi.close()

      #change_to_UDP
      morse_list=[Morse(fi[temp][0],fi[temp][1]) for temp in range(0,len(fi))]
      

      return morse_list
   

#Question3

def output_MorseCode(temp_li):
          li =[print(temp_li[line]) for line in range(0,len(temp_li))]
   
      

#Question4
class Morse:
   
      def __init__(self,x,y):
         self.signal=x
         self.morse=y

      def __str__(self):
         return '%s represents %s'% (self.signal,self.morse)

       # This function is the answer 
      def __lt__(self,others):
         ord(str(self.signal)) < ord(str(others.signal))
         return True

      def __eq__(self,others):
            self.morse==others.morse
            return True
      

#Question5

def readfile():

         filename=("MorseCode.csv")
         fi=open(filename)
         li=[line.split(",") for line in fi.readlines()]
         fi.close()
         return li

def search(char):
      fi=readfile()

      temp_list=[print(fi[line][1])  for line in range(0,len(fi)) if char ==fi[line][0]]
       


      

      

   

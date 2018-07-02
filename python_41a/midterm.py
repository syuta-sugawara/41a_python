#Write your test number here: Version#3 midterm spring'18
#Answer 1:

class Morse:
        def __init__(self,x,y):
                self.signal=x
                self.morse=y

        def __str__(self):
                return '%s represents %s'% (self.signal,self.morse)

        def string_conversion(self):
                return str(self.signal) + str(self.morse)

#Answer 2:

class Morse:

        def __init__(self,x,y):
                self.signal=x
                self.morse=y

        def __str__(self):
                return '%s represents %s'% (self.signal,self.morse)

        def string_conversion(self):
                return str(self.signal) + str(self.morse)

#This is the answer
        def readfile_change_to_Morse_UDT():
        #file_read
                filename=("MorseCode.csv")
                fi=open(filename)
                li=[]
                for line in fi.readlines():
                        li.append(line.split(","))
                fi.close()

#change_to_UDP
                morse_list=[]
                for temp in range(0,len(fi))
                        morse_list.append(temp=Morse(fi[temp][0],fi[temp][1]))
                return morse_list

#Answer 3:

def output_MorseCode(temp_li):
        for line in range(0,len(temp_li)):
                print(temp_li[line])

 

#Answer 4:

class Morse:

        def __init__(self,x,y):
                self.signal=x
                self.morse=y

        def __str__(self):
                return '%s represents %s'% (self.signal,self.morse)

        def string_conversion(self):
                return str(self.signal) + str(self.morse)

# This function is the answer 
        def __lt__(self,others):
                return ord(str(self)) < ord(str(others))

#Answer 5:

def readfile():
        li=[]
        filename=("MorseCode.csv")
        fi=open(filename) 
        for line in fi.readlines():
        li.append(line.split(","))
        fi.close()
        return li

def search(char):
        fi=readfile()
        for line in range(0,len(fi)):
        if char ==fi[line][0]:
        return fi[line][1]

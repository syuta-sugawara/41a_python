
def readfile():
      li=[]
      file_name="UProducts.csv"
      file=open(file_name,"r")

      for line in file.readlines():
            line
            li.append(line.split(","))      
      file.close()
      li.sort()
      return li

def crate_alphabet_list():
      master_list=[]
      for temp in range(0,25):
         master_list.append([])
      return master_list

def index(temp_string):

      return ord(temp_string) - ord("A")


def insert_master_list():
      file_list=readfile()
      master_list=crate_alphabet_list()
      print(master_list)

      for line in range(0,len(file_list)):

            char=file_list[line][0][0]
            unicode_num=index(char)

            master_list[unicode_num].append(file_list[line])


      print(master_list)
      for temp in range(0,len(master_list)):
            master_list[temp].sort()

      return master_list

master_list=insert_master_list()
search=input("Enter full name which you want to search  ")
temp_num=index(search[0])
master_list[temp_num]

for a in range(0,len(master_list[temp_num])):
            if search in master_list[temp_num][a]:

                       print('the position of what you want t search is %i in [%s] list'% (a+1,search[0]) )
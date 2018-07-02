
def crate_alphabet_list():
      master_list=[{} for temp in range(0,25)]
      return master_list

def index(temp_string):
      return ord(temp_string) - ord("A")

def readfile_insert():

      master_list=crate_alphabet_list()
      file_name="UProducts_1.csv"
      file=open(file_name,"r")
      li=[x for x in file.readlines()]
      li.sort()

      for line in li:
          temp={line.split(",")[0] : line.split(",")[1]}
          char=line.split(",")[0][0]
          unicode_num=index(char)
          master_list[unicode_num].update(temp)
      file.close()

      return master_list

master=readfile_insert()

print(master)

search=input("Enter full name which you want to search  ")
for line in range(0,len(master)):
            if search in master[line].keys():
                       print('the price is $ %s'% (master[line].get(search)) )






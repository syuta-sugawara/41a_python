def is_triangle(x,y,z):
   if x<y+z and y<x+z and z<x+y  :
      print("Yes")3
      4
   else :
      print("No")
   
def get_stick():
   x=int(input("Enter the first stick lengths :"))
   y=int(input("Enter the second stick lengths :"))
   z=int(input("Enter the third stick lengths:"))
   is_triangle(x,y,z)

get_stick()

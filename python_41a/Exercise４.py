#Syuta Sugawara

"""
Exercise 7.3.
Write a function named test_square_root that prints a table
like this:
1.0 1.0 1.0 0.0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
3.0 1.73205080757 1.73205080757 0.0
4.0 2.0 2.0 0.0
5.0 2.2360679775 2.2360679775 0.0
6.0 2.44948974278 2.44948974278 0.0
7.0 2.64575131106 2.64575131106 0.0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0 3.0 0.0

The first column is a number, a; the second column is
the square root of a computed with the function from Section 7.5;
the third column is the square root computed by math.sqrt;
the fourth column is the absolute value of the difference
between the two estimates.
"""
import math
epsilon=0.0000001
def newton_method(a,x):
      while True:
         y = (x + a/x)/2
         if abs(y-x) < epsilon:
            return x
         x = y
length=int(input("Enter the number :"))


for a in range(1,length):
      float_a=float(a)
      b=float_a+1.0
      second=newton_method(float(a),b)

      print(float_a,second,math.sqrt(float_a),second-math.sqrt(float_a))





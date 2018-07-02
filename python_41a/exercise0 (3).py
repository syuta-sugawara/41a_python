#Syuta Sugawara


"""
1. Open IDLE from the classroom computer.
At the shell, write a Python statement to print
"Hello world!" on one line and then print "this is <your name>"
on the next line.
Paste your script into your answer.
"""
print('"Hello world!"')
name="Syuta"
print("This is",name)


"""
2. Run this script to see the output:
"""
"""

num = input("Enter a number: ")
print(num)
num + 5
"""

"""

Enter a number: 3
3
Traceback (most recent call last):
  File "/Users/sugawarasyuta/Desktop/hello.py", line 8, in <module>
    num + 5
TypeError: must be str, not int
"""


"""
3. Fix the problem in question 2.
"""

"""
1. The volume of a sphere
with radius r is 4/3 pi r^3 (see text book for proper formula).
What is the volume of a sphere with radius 5?
"""


import math
r=5
sphere = (4/3)*math.pi*(r**2)
print(sphere)

#answer 104.71975511965977

"""
2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?
"""

first=24.95*0.6+3
secondFollowing=24.95*0.6+ 0.75
total=first+(59*secondFollowing)
print(total)

#answer 945.4499999999999




"""
If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, 
what time do I get home for breakfast?
"""


currentHours = 6
currentMinutes = 52
easyMinutes = 8
easySec = 15
tempoMinutes= 7
tempoSec = 12
easyMiles = 2
tempoMiles = 3

easyTime = (easyMinutes * 60 + easySec) * easyMiles 
tempoTime = (tempoMinutes* 60 + tempoSec) * tempoMiles
runTime = easyTime + tempoTime

currentTime =currentHours* 3600 + currentMinutes *60
endTime = currentTime + runTime

endHours = endTime//3600
endMinutes = (endTime % 3600) // 60

print(endHours, ':', endMinutes)

#Answer 7 : 30 AM



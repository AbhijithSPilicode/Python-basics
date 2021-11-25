Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"modules"
'modules'
import math
help(math)

sqrt(64)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    sqrt(64)
NameError: name 'sqrt' is not defined
math.sqrt(64)
8.0
math.pi
3.141592653589793
math.gcd(12,20,6)
2
import time
time.time
<built-in function time>
time.time()
1636359410.9898853
import os
os.getcwd()
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python310-32'
import random
random.randint(12,15)
15

random.randint(12,15)
14
random.randint(12,15)
15
random.randint(12,15)
13
import calender
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
import calendar
calendar.month(2021,11)
'   November 2021\nMo Tu We Th Fr Sa Su\n 1  2  3  4  5  6  7\n 8  9 10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30\n'
print(calendar.month(2021,11))
   November 2021
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30

import math as m
math.sqrt(64)
8.0
m.sqrt(64)
8.0
print(calendar.month(2000,3))
     March 2000
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31


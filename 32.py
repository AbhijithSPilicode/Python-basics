Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
animals=["dog","cat"]
animals.append("wolf")
animals
['dog', 'cat', 'wolf']
animals.insert(1,"horse")
animals
['dog', 'horse', 'cat', 'wolf']

=============== RESTART: C:/Users/user/Desktop/asap/python/31.py ===============
Traceback (most recent call last):
  File "C:/Users/user/Desktop/asap/python/31.py", line 7, in <module>
    rev.insert(0,a[var])
NameError: name 'a' is not defined

=============== RESTART: C:/Users/user/Desktop/asap/python/31.py ===============
['redmi', 'iphone', 'samsung', 'nokia']
b=animals.copy()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    b=animals.copy()
NameError: name 'animals' is not defined
animals
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    animals
NameError: name 'animals' is not defined
animals=["dog","cat"]
b=animals.copy()
b
['dog', 'cat']
c=animals.clear()
c
b.append("dog")
b.append("dog")
b.append("dog")
b
['dog', 'cat', 'dog', 'dog', 'dog']
b.count("dog")
4
b.extend(["horse","elephant","wolf"])
b
['dog', 'cat', 'dog', 'dog', 'dog', 'horse', 'elephant', 'wolf']
b.index("horse")
5
b.index("dog")
0
b.index("dog",1)
2
b.index("dog",1,8)
2
b.index["dog",3] #starts from 3rd position
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b.index["dog",3] #starts from 3rd position
TypeError: 'builtin_function_or_method' object is not subscriptable
b.index("dog",3)
3
b.remove("wolf")
b
['dog', 'cat', 'dog', 'dog', 'dog', 'horse', 'elephant']
b.pop(-1) #remove last item  #pop(index)
'elephant'
b
['dog', 'cat', 'dog', 'dog', 'dog', 'horse']
var=12
del(var)
del(b[3])
b
['dog', 'cat', 'dog', 'dog', 'horse']
num=[23,5,3,2,4,567,45,1]
#reverse list
num.reverse()
num
[1, 45, 567, 4, 2, 3, 5, 23]
#sort
num.sort(reverse=True)
num
[567, 45, 23, 5, 4, 3, 2, 1]
name=["Dhoni","sachin","althaf","zaheer khan","XAVIER"]
name.sort()
name
['Dhoni', 'XAVIER', 'althaf', 'sachin', 'zaheer khan']
name.append("ALTHAF")
name.append("Althaf")
name.sort()
name
['ALTHAF', 'Althaf', 'Dhoni', 'XAVIER', 'althaf', 'sachin', 'zaheer khan']

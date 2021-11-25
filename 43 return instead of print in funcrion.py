Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def add(x,y):
    print(x+y)

    
add(12,2)
14
def add(x,y):
    return x+y

a=add(12,2)
# if using return statement we have to assign it into a variable when calling the function
print(a)
14
print(a+100)
114
print(add(45+5))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(add(45+5))
TypeError: add() missing 1 required positional argument: 'y'
print(add(45,5))
50

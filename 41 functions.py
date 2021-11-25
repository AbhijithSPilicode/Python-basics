Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
len
<built-in function len>
type(len)
<class 'builtin_function_or_method'>
len="i am not the len you are looking for"
len
'i am not the len you are looking for'
del(len)
len
<built-in function len>
count=len("python")
count
6
# function
def greet(name):
    print(f"hello {name}")

    

greet()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    greet()
TypeError: greet() missing 1 required positional argument: 'name'
greet("unstoppable")
hello unstoppable
def shout(string):
    string=string.upper()
    print(string)

    
shout("python")
PYTHON
word="programming"
shout(word)
PROGRAMMING

=============== RESTART: C:/Users/user/Desktop/asap/python/42.py ===============
enter a number:6
enter second number:8
14

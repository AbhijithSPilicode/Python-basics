Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def test(fun,x):
    return fun(fun(x))
test(lambda x:x*5,4) 

    
SyntaxError: invalid syntax
def test(fun,x):
    return fun(fun(x))

test(lambda x:x*5,4) 

100
test(lambda x:x+100,4)
204
none
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    none
NameError: name 'none' is not defined. Did you mean: 'None'?
None
type(None)
<class 'NoneType'>
a=lambda x:True if x>100 else False
a(12)
False
a(120)
True
b=lambda x,y:x**2 + 2*x*y +10
b(2,3)
26
c=lambda word:True if wodr==word[::-1] else False
c("python")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    c("python")
  File "<pyshell#13>", line 1, in <lambda>
    c=lambda word:True if wodr==word[::-1] else False
NameError: name 'wodr' is not defined
c=lambda word:True if word==word[::-1] else False
c("python")
False
c("level")
True

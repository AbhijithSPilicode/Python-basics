Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#arguments
def test(x+y):
    
SyntaxError: invalid syntax
def test(x,y)
SyntaxError: expected ':'
def test(x,y):
    print(x+y)

    

test(12,2)
14
test(12)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    test(12)
TypeError: test() missing 1 required positional argument: 'y'
test(12,2,3)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    test(12,2,3)
TypeError: test() takes 2 positional arguments but 3 were given
def info(name,age,course):
    print("name:",name)
    print("age:",age)
    print("course:",course)

    
info("stem",4,"python")
name: stem
age: 4
course: python
#keyworded arguments
info(age=4,course="python",name="stem")
name: stem
age: 4
course: python
#argument three type: keyword arguments,positional arguments,required arguments
def info(name,age,course="python"):
    print("name:",name)
    print("age:",age)
    print("course:",course)

    
info("stem",4)
name: stem
age: 4
course: python
info("stem",4,"c++")
name: stem
age: 4
course: c++
def test(x,y=100):
    print(x+y)

    
test(12)
112
test(12,2)
14
#variable length arguments
def test(x,y,*z):
    print(x)
    print(y)
    print(z)

    
test(12,2)
12
2
()
test(12,2,100)
12
2
(100,)
test(12,2,100,200,300,400)
12
2
(100, 200, 300, 400)
def info(name,age,course="python",*addr):
    print("name:",name)
    print("age:",age)
    print("course:",course)
    if addr!=():
        print("ADDRESS:",addr)

        
info("stem",4,"python","ullor","trivandrum")
name: stem
age: 4
course: python
ADDRESS: ('ullor', 'trivandrum')
list((12,23,34))
[12, 23, 34]
a,b,*c=12,23,34,45,56
a
12
b
23
c
[34, 45, 56]
def add(x,y):
    return x+y

print(add(12,2))
14
add
<function add at 0x03404FA0>
addition=add
addition
<function add at 0x03404FA0>
print(addition(100,200))
300
def test(fun,x):
    print("-" * 25)
    fun(x)
    print("-" * 25)

    

greet("stem")
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    greet("stem")
NameError: name 'greet' is not defined
def greet(name):
    print("Hello",name)

    
greet("stem")
Hello stem
def test(fun,x):
    print("-" * 25)
    fun(x)
    print("-" * 25)

    
test(greet,"stem")
-------------------------
Hello stem
-------------------------
def fun(x):
    return x*5

def do_twice(f,y):
    return f(f(y))

print(do_twice(fun,4))
100
def f1(x):
    return (x**2)

print(do_twice(f1,4))
256

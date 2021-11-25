Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"docstrings"
'docstrings'
def test(name):
    """ test will take a name and greet hello"""
    print("Hello",name)

    
help(test)
Help on function test in module __main__:

test(name)
    test will take a name and greet hello

print(test.__doc__)
 test will take a name and greet hello
len.__doc__
'Return the number of items in a container.'
nums=[12,23,25]
sum(nums)
60
min(nums)
12
max(nums)
25
sum((12,23,35))
70
string="12,23,34,89,90"
list1=string.split(",")
list1
['12', '23', '34', '89', '90']
list1[0]+100
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list1[0]+100
TypeError: can only concatenate str (not "int") to str
int(list1[0])+100
112
list1=string.split(" ")
list1
['12,23,34,89,90']

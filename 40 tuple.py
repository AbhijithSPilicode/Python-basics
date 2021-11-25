Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#tuple type of data
#tuple type is immutable
#tuple type data can be made by paranthesis
nums=(12,23,34)
type(nums)
<class 'tuple'>
nums[0]
12
nums[1]
23
nums[1]=90
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    nums[1]=90
TypeError: 'tuple' object does not support item assignment
nums=912,2,33,34,350
nums=(912,2,33,34,350)
for i  in nums:
    print(i)

    
912
2
33
34
350
numbers=912,2,33,34,350
type(numbers)
<class 'tuple'>
#tuple packing and unpacking
items=(100,200,300)
a,b,c=items
a
100
b
200
c
300
x=10
y=20
x,y=y,x
x
20
y
10

t1=(1,2,3,4,5)
t2=(100,200,300,400,500)
print(tuple(zip(t1,t2)))
((1,100),(2,200),(3,300),(4,400),(5,500))

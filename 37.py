Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#loop inside a loop
list1=[[12,"python",23.34],["stem","programming",34],[True,"robotics",56.78]]
list1[2]
[True, 'robotics', 56.78]
list1[0][1]
'python'
for i in list1:
    for j in i:
              print(j)

              
12
python
23.34
stem
programming
34
True
robotics
56.78
for i in range(1,4):
    for j in range(4,7):
        print(f"the value of i={i}\t the value of {j}=j")

        
the value of i=1	 the value of 4=j
the value of i=1	 the value of 5=j
the value of i=1	 the value of 6=j
the value of i=2	 the value of 4=j
the value of i=2	 the value of 5=j
the value of i=2	 the value of 6=j
the value of i=3	 the value of 4=j
the value of i=3	 the value of 5=j
the value of i=3	 the value of 6=j
for i in range(1,4):
    for j in range(4,7):
        print(f"the value of i={i}\t the value of j={j}")

        
the value of i=1	 the value of j=4
the value of i=1	 the value of j=5
the value of i=1	 the value of j=6
the value of i=2	 the value of j=4
the value of i=2	 the value of j=5
the value of i=2	 the value of j=6
the value of i=3	 the value of j=4
the value of i=3	 the value of j=5
the value of i=3	 the value of j=6

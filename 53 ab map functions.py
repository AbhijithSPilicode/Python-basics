Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#map function
nums=[1,2,3,4,5,6,7,8,9,10]
a=map(lambda x:x+100,nums)
a=list(a)
print(a)
[101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
print(list(map(lambda x:x*2,nums)))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(tuple(map(lambda x:x*2,nums)))
(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
#1.WAP to get a list of numbers from the user and find the cube of each number
nums=[1,2,3,4,5]
nums=[1,2,3,4,5]
b=list(map(lambda x:x ** 3,nums))
b
[1, 8, 27, 64, 125]
#2.WAP to get a list of words from the user and capitalise each word
word=["python","programming","map","lambda","function","return"]
c=list(map(lambda x:x.upper(),words))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    c=list(map(lambda x:x.upper(),words))
NameError: name 'words' is not defined. Did you mean: 'word'?
c=list(map(lambda x:x.upper(),word))
c
['PYTHON', 'PROGRAMMING', 'MAP', 'LAMBDA', 'FUNCTION', 'RETURN']
#WAP to get a list of words from user and print the reverse of each word

#4.WAP to get a list of words from user and print the length of each word
words=["python","programming","map","lambda","function","return"]
e=list(map(lambda x:len(x),words))
e
[6, 11, 3, 6, 8, 6]
#WAP to get a list of words from user and print the reverse of each word

words=["python","programming","map","lambda","function","return"]
f=list(map(lambda x:x[::-1],words))
f
['nohtyp', 'gnimmargorp', 'pam', 'adbmal', 'noitcnuf', 'nruter']

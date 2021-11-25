Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
##lambda functions
#1.WAP to get a word from user and capitalize it using lambda syntax
a=lambda x:x.upper()
a("python")
'PYTHON'
#2.WAP to get a number from user and return true if it is even else false using lambda syntax

a=lambda x:True if x%2==0 else False
a(12)
True
a(17)
False
#3.WAP to check if a word is upper case using lambda syntax

b=lambda x:True if x==x.upper()
SyntaxError: expected 'else' after 'if' expression
b=lambda x:True if x==x.upper() e;se False
SyntaxError: expected 'else' after 'if' expression
b=lambda x:True if x==x.upper() else False
b("python")
False
b("PYTHON")
True
#4.WAP to check if a number is integer using lambda syntax
c=lambda x True if x>0 else False if x==0 else False
SyntaxError: invalid syntax
c=lambda x:True if x>0 else False if x==0 else False
a(0)
True
c(0)
False
c(-2)
False
c(2)
True
#6.WAP to get a number from user and check if it is positive using lambda syntax is above
#4.WAP to check if a number is integer using lambda syntax
d=lambda x:x.is_integer()
d(2.00)
True
d(2.46)
False
#5.WAP to get a word from the user and print the length of the word using lambda syntax

e=lambda x:len(x)
e("python")
6
e("messi")
5

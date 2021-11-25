Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#leetspeak
word=input("enter the word:")
enter the word:Loef Haxor
word.replace("a",4)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    word.replace("a",4)
TypeError: replace() argument 2 must be str, not int
word.replace("a","4")
'Loef H4xor'
word .replace("b","8")
'Loef Haxor'
word.replace("e","3")
'Lo3f Haxor'
word.replace("l","1")
'Loef Haxor'
word.replace("o","0")
'L0ef Hax0r'
word.replace("s","5")
'Loef Haxor'
word.replace("t","7")
'Loef Haxor'

============ RESTART: C:/Users/user/Desktop/asap/python/11 to 10.py ============
enter the word:Loef Haxor
Traceback (most recent call last):
  File "C:/Users/user/Desktop/asap/python/11 to 10.py", line 2, in <module>
    word.replace("a",4)
TypeError: replace() argument 2 must be str, not int

============ RESTART: C:/Users/user/Desktop/asap/python/11 to 10.py ============
enter the word: Loefb Haxora
Traceback (most recent call last):
  File "C:/Users/user/Desktop/asap/python/11 to 10.py", line 2, in <module>
    word.replace("a",4)
TypeError: replace() argument 2 must be str, not int

============ RESTART: C:/Users/user/Desktop/asap/python/11 to 10.py ============
enter the word:Loef Haxor
L03f H4x0r
 round(2.33333)
 
SyntaxError: unexpected indent
round(2.33)
2
round(4.78)
5
round(3.5)
4
round(2.3333333,2)
2.33
round(6.456,2)
6.46
abs(-2)
2
abs(0)
0
pow(2,3)
8
pow(8,-3)
0.001953125
#exponential function
power(9,1/2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    power(9,1/2)
NameError: name 'power' is not defined
pow(9,1/2)
3.0
num=3.0
num.is_integer()
True
num=3.01
num.is_integer()
False

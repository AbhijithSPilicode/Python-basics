Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
side=float(input("enter side of cube:"))
enter side of cube:3
volume=side ** 3
volume
27.0
num1=12
num2=10
print(f"the volume of num1 is {num1} and the value  of num2 is{num2}.")
the volume of num1 is 12 and the value  of num2 is10.
#string formatting
#to avoid the problem of datatype
num1=12.23333333
result=num1+num2
print(f"(num1:.2f) + (num2:.2f) = result :.2f)")
(num1:.2f) + (num2:.2f) = result :.2f)



word="python is a high level language"
words.find("level")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    words.find("level")
NameError: name 'words' is not defined. Did you mean: 'word'?
word.find("level")
17
word.find("   python")
-1
words=int(input("enter the word"))
enter the word i was watching the movie home last week
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    words=int(input("enter the word"))
ValueError: invalid literal for int() with base 10: ' i was watching the movie home last week'
words=input("enter the word")
enter the word i was watching the movie home last week
word.find("home")
-1
words.find("home")
26
#to find a substring from a string
words.replace("home","kuruthi")
' i was watching the movie kuruthi last week'
#replacing a substring

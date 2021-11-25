import os
os.chdir("C:\\Users\\user\\Desktop\\asap")

try:
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))
    res =num1/num2
    print(res)
except ZeroDivisionError:
    print("division by zero is not possible")
except ValueError:
    print("non integer value")
else:
    print("this will be printed if there is no exception")
finally:
    print("program finished")    
    
#if you give stem or a word or a letter or anything other than integer as input it will give non integer value as output.
#if you give zero as num2 it will give division by zero is not possible.    
try:
    file=open("qwerty.txt","r")
    s=file.read()
    print(s)
except:
    print("something is wrong!")
finally:
    file.close()
print(s)


             

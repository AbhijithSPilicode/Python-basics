#calculator
num1=int(input("enter first number:"))
num2=int(input("enter the second number:"))
fun_1=input("enter the function")
if(fun_1=="+"):
    fun=num1+num2
    print(f"{fun}")
elif(fun_1=="-"):
    fun=num1-num2
    print(f"{fun}")
elif(fun_1=="*"):
    fun=num1*num2
    print(f"{fun}") 
elif(fun_1=="/"):
    fun=num1/num2
    print(f"{fun}") 
elif(fun_1=="^"):
    fun=num1 ** num2
    print(f"{fun}") 
else:
    print("invalid")





    
#and 0*0=0,0*1=0,1*0=0,1*1=1,anyone false,it is false

#or 0+0=0,0+1=1,1+0,1,1+1=1    

year=int(input("enter a year"))
if year%400==0 or (year%4==0 and year%100!=0):
 print(f"{year} is a leap year")
else:
 print(f"{year} is not aleap year")




#WAP to admit only kids whose age is less than 14 and greater than 8 or whose height is more than 120cm and less than 150cm to a particular ride in an amusement park.

age=int(input("enter an age"))
height=int(input("enter the height"))
if (age>8 and age <14) or (height>=120 and height<=150):
 print("eligible for ride")
else:
 print(f"not eligible for ride")





 #WAP to get a character from the user and print whether its a vowel or a 	consonant.


char=input("enter the charactor:").lower()

if (char=="a") or (char=="e") or (char=="i") or (char=="o") or(char=="u") :
    print("enterd charactor is a vowel")
else:
    print("it is a consonent")


#method2
char_1=input("enter the charactor:").lower()
if "aeiou".find(char_1)!=-1:
     print("vowel")
else:
     print("not vowel")



     

    

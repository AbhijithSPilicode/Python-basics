var_1=int(input("enter a length"))
var_2=int(input("enter a width"))
if var_1>0:
    print(f"value is {var_1} is a positive number")
if var_1%2==0:
    print(f"value is {var_2} is an even number")
if var_1==var_2:
    print(f"value is of a square")
age_1=int(input("enter a age1"))
age_2=int(input("enter a age2"))
if (age_1>age_2):
    print(f"{age_1} is elder")
if(age_2>age_1):
    print(f"{age_2} is elder")
word=(input("enter a string"))
char=input("enter a chara")
if word.startswith(char):
    print(f"{word} start with {char}")

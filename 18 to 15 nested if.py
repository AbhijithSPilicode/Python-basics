#nested if
num=int(input("enter a number"))
if num>0:
    print(f"{num} is positive")
    if num%5==0:
        print(f"{num} is multiple of 5")
    else:
        print(f"{num} is not a multiple of 5")

else:
    if num==0:
        print(f"{num} is zero")
    else:
        print(f"{num} is negative number")
         
        

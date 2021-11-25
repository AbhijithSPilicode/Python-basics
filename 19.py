#else-if ladder
num=int(input("enter a number"))
if num%5==0:
        print(f"{num} is multiple of 5 and 2")
else:
    if num%2==0:
        print(f"{num} is  a multiple of 2")
    else:       
        if num%5==0:
         print(f"{num} is a multiple of 5")


#elif ladder
digit=int(input("enter a digit"))
if(digit==1):
    print("monday")
elif(digit==2):
    print("tuesday")
elif(digit==3):
    print("wednesday")
elif(digit==4):
    print("thursday")
elif(digit==5):
    print("friday")
elif(digit==6):
    print("saturday")
elif(digit==7):
    print("sunday")
else:
    print("invalid")   
         
        

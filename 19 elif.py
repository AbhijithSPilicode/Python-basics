#else-if ladder
num=int(input("enter a number"))
if num%10==0:
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


#WAP to get a number from the user and check if it is a multiple of both 5 and 2, if so print its "multiple of both5 and 2",else you have to check if its either multiple of 5 or 2,
    #and print according to the condition, else, print" not a multiple of 5 nor 2"
    


num_2=int(input("enter a number"))
if num_2%10==0:
        print(f"{num_2} is multiple of 5 and 2")
elif num_2%2==0:
        print(f"{num_2} is  a multiple of 2")
elif num_2%5==0:
         print(f"{num_2} is a multiple of 5")
else:
    print("not multiple of 5 and not multiple od 2")




#A year may be a leap year if it is evenly divisible by 4. Years that are divisible by 100 (century years such as 1900 or 2000) cannot be leap years unless they are also divisible by 400.
#For this reason, the years 1700, 1800, and 1900 were not leap years, but the years 1600 and 2000 were.)


num_3=int(input("enter a year"))
if num_3%400==0:
        print(f"{num_3} is a leap year")
elif num_3%100==0:
        print(f"{num_3} is not a leap year")
elif num_3%4==0:
         print(f"{num_3} is  a leap year")
else:
    print(f"{num_3}not a leap year")

    
        

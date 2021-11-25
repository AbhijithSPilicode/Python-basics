#calculator in break

while True:
 opt=int(input("enter a number"))
 num1=int(input("enter a number:"))
 num2=int(input("enter second number:"))
 if opt==1:
         res= num1+num2
         print(f"{num1} + {num2} = {res}")
 elif opt==2:
         res= num1-num2
         print(f"{num1} - {num2} = {res}")
 elif opt==3:
         res= num1 *num2
         print(f"{num1} * {num2} = {res}")         
 elif opt==4:
         res= num1/num2
         print(f"{num1} / {num2} = {res}")
 elif opt==5:
         break
else:
    print("invalid")

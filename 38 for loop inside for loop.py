#get two numbers and multiplication table in between that range
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
for i in range(num1,num2+1):
    for j in range(11):
         print(f"{j} x {i} ={i*j}")

#factorial
num3=int(input("enter number1:"))
fact=1
for i in range(1,num3+1):
    fact*=i
print(f"factprial of {num3} is {fact}")

         
#break
for i in range(11):
    print(i)
    if i==6:
          break
else:
    print("run without break")
    
    
        
for i in range(11):
    print(i)
   # if i==6:                      #it will execute until 10 and print command
    #      break
else:
    print("run without break")

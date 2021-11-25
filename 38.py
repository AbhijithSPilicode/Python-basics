#get two numbers and multiplication table in between that range
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
for i in range(num1,num2+1):
    for j in range(11):
         print(f"{j} x {i} ={i*j}")

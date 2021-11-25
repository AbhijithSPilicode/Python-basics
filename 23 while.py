#while loop
var_1=1
while var_1<=5:
    print("loop")
    var_1=var_1+1

#even numbers usig while loop
var_2=2
while var_2<=100:
     print(var_2,end=",")
     var_2=var_2+2

#1-WAP to print all the odd numbers from 100 till zero.
var_3=99
while var_3>=0:
       print(var_3,end=",")
       var_3=var_3 -2

#2-WAP to get a two digit number from the user and print all the numbers from that number till 100
var_4=int(input("enter a number"))
while var_4<=100:
        print(var_4,end=",")
        var_4=var_4+1

#3-WAP to get a two digit number from the user and print all the even numbers from 100 till that number

var_5=int(input("enter a number"))
var_6=100
while var_6>=var_5:
        print(var_6,end=",")
        var_6=var_6-2
        
#4-WAP to print all the multiples of 5 from 0 till 250
var_7=0
while var_7<=250:
 print(var_7,end=",")
 var_7+=5
 
#5-WAP to get a number from the user and print all the multiples of 3 from that number till 100.
var_8=int(input("enter a number"))
while var_8<=100:
    if var_8%3==0:
        print(var_8,end=",")
    var_8=var_8+1
    
#6-WAP to get 10 marks from a student and find the total and the average.
var_9=1
total_1=0
while var_9<=10:
    mark=int(input("enter mark:"))
    total_1+=mark
    var_9+=1
print(f"total={total_1} and average={total_1/10}")

#7-WAP to get 5 ages from the user and find the eldest one
var_10=1
elder=0
while var_10<=5:
    age=int(input("enter age:"))
    if(age>elder):
        elder=age
    var_10+=1
print(f"elder age is {elder}")
        

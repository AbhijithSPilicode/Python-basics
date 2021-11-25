#make a list of car from user  and print all item start with L or l.
cars=[]
var=0
limit=int(input("how many items you want in list?"))
while var<limit:
    item=input(f"enter car:")
    cars+=[item]
    var+=1
num=0
while num<len(cars)-1:
    if cars[num][0]=="l" or cars[num][0]=="L":
     print(cars[num])
    num+=1



#make a list of animal from user and print whose name is less than or equal to 4
animals=[]
var1=0
limit1=int(input("how many items you want in list?"))
while var1<limit1:
    item1=input(f"enter animals:")
    animals+=[item1]
    var1+=1
num1=0
while num1<len(animals)-1:
    if len(animals[num1])<=4:
     print(animals[num1])
    num1+=1    
#list of number from user and print even number greater than 50
numbers=[]
var2=0
limit2=int(input("how many items you want in list?"))
while var2<limit2:
    item2=int(input(f"enter numbers:"))
    numbers+=[item2]
    var2+=1
    if(item2>50):
        if(item2%2==0):
              print(item2)
          

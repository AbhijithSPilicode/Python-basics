#reverse list using insert method
mobile=("nokia","samsung","iphone","redmi")
length=len(mobile)
var=0
rev=[]
while(var<length):
    rev.insert(0,mobile[var])
    var+=1

print(rev)    


    
cars=[]
limit=int(input("enter limit:"))
var1=0
while var1<limit:
    item=input("enter a car:")
    cars.append(item)
var1+=1
cars.sort()
v=0
while v<len(cars):
    print( cars[v],end=",")
    v+=1
    
          



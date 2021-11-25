#list
fruits=["apple","orange","banana","mango","watermelon","strawberry","cashewnut","jackfruit"]
#to print elements in a list
limit=len(fruits)-1
var=0
while var<=limit:
    print(fruits[var])
    var+=1
#
cars=[]
var=0
limit1=int(input("how many items you want in list?"))
while var<limit:
    item=input(f"enter car{var+1}:")
#string cannot add with list...so we have to give the string in square bracket to list
    cars+=[item]
    var+=1
print(cars)    


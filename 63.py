from array import *
a=[]
var=0
limit=int(input("how many items you want in list?"))
while var<limit:
    item=input(f"enter array element:")
    a+=[item]
    var+=1
for i in range(len(a)-2):
    for j in(i+1,len(a)-1):
        if a[j]<a[i]:
            a[i],a[j]=a[j],a[i]
print(a)            

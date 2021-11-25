#Arrays
from array import * #importing everything in array module
nums=array("i",[12,23,34,45,56,67,78,89,90]) #i for integers
print(nums)
print(type(nums))


for i in nums:
    print(i)

print(nums[0])

nums[0]=123
print(nums[0])

nums.remove(56)
print(nums)
nums.insert(4,400) #400 will be the new item at 4th position and others shift to right
print(nums)

#get list of integer from user and create an array and print the array without using sort function
a=[]
var=0
limit=int(input("how many items you want in list?"))
while var<limit:
    item=input(f"enter array element:")
    a+=[item]
    var+=1

new_list=[]

while a:
    minimum = a[0]  
    for x in a: 
        if x < minimum:
            minimum = x
    
    new_list.append(minimum)
    a.remove(minimum)    

print(new_list)

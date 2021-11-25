#WAP to get a list from the user and using function, remove the duplicate and print the new list onto screen using return

def rem_duplicate(list1):
    new=[]
    for item in list1:
        if item not in new:
            new.append(item)
    print(new)        
def get_list():
    nums=[]
    limit=int(input("enter limit:"))
    for j in range(limit):
        item=int(input("enter item:"))
        nums.append(item)
    return nums
    
list_2=get_list()
rem_duplicate(list_2)
list_3=get_list()
print(list_3)

#
def test():
    x=12
    y=100
    z=200
    return x,y,z
a,b,c=test()
print(a)
print(b)
print(c)

#
def get_list1():
    new=[]
    limit=int(input("enter number of item in list:"))
    for i in range(limit):
        item=int(input("enter number:"))
        new.append(item)
    return new
def print_evens(list1):
    for i in list1:
        if i%2==0 and i>50:
            print(i)
s=get_list1()
print_evens(s)
    

fruits=["apple","grape","mango","banana","cherry","kiwi"]
print("apple" in fruits)
print("grape" not in fruits)

#
mobile=["samsung","nokia","micromax","iphone","redmi","realme","oppo","vivo"]
item=input("enter an item:")
if( item in mobile):
    print(f"{item} is present in list mobile")
else:
    print(f"{item} is not present in the list")
    
revlist=mobile[::-1] #reversing a list
print(revlist)



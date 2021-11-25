#WAP to get a list of numbers from the user and print the numbers greater than 50.
number=[]
limit=int(input("enter number of item:"))
for i in range(limit):
    item=int(input("enter item:"))
    number.append(item)
for number in number:
    if(number>50):
        print(number)
#WAP to get a list off numbers from the user and print only the even numbers

number1=[]
limit1=int(input("enter number of item:"))
for j in range(limit1):
    item1=int(input("enter item:"))
    number1.append(item1)
for number1 in number1:
    if(number1%2==0):
        print(number1)        
#WAP to get a list of numbers from the user and print all the multiples of 3 in ascending order
number2=[]
limit2=int(input("enter number of item:"))
for k in range(limit2):
    item2=int(input("enter item:"))
    number2.append(item1)
for number2 in number2:
    if(number2%3==0):
        print(number2)

#WAP to get a list of city names from user and print all the names which has more than 8 characters, in ascending order


names=[]
limit=int(input("enter the number of item:"))
for i in range(limit):
    item=input("enter the name:")
    names.append(item)
names.sort()
for names in names:
    if len(names)>8:
        print(names)
        

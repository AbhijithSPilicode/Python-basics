#functions
#def name():
#add and multiply 2 numbers using function
def add(num1,num2):
    print(num1 + num2)
def product(num1,num2):
    print (num1*num2)

var_1=int(input("enter a number:"))
var_2=int(input("enter second number:"))
add(var_1,var_2)
product(var_1,var_2)


#radius of sphere and volume of it using function
def volume(radius):
    volume=(4/3)*(3.14)*(radius ** 3)
    print(volume)
var_3=int(input("enter radius:"))
volume(var_3)

#WAP to get the length and width of a rectangleand find the area and perimeter using functions and print onto screen.

def area(a, b):
    return (a * b)
 
def perimeter(a, b):
    return (2 * (a + b))
 
l = float(input("Enter length: ")) 
b = float(input("Enter breadth: ")) 
print ("Area = ", area(l, b))
print ("Perimeter = ", perimeter(l, b))



#WAP to get a temperature reading in celcius from the user and using function, convert into farenheit scale and print onto screen.

def farrenheit(celcius):
    farrenheit=(celcius*(9/5))+32
    print(farrenheit)
var_6=int(input("enter temp in celcius"))
farrenheit(var_6)

#WAP to get a number from the user and using function, find the factorial of that number and print onto the screen.
def factorial(num):
    f=1
    for i in range(1,num+1):
        f*=i
    print("factorial is",f)
var_7=int(input("enter a number:"))
factorial(var_7)


#WAP to get a number from the user and using function check if it is positive or negetive
def positive(num):
    if(num>0):
        print("positive")
    else:
        print("negative")
var_8=int(input("enter a number:"))
positive(var_8)

#WAP to get a list of names from user and using a function, capitalize each item and print the new list

def capitalize(list2):
    new1=[]
    for item in list2:
            item=item.upper()
            new1.append(item)
            print(item)        
word=[]
limit1=int(input("enter limit:"))
for j in range(limit1):
    item=(input("enter item:"))
    word.append(item)
capitalize(word)


#WAP to get a list from the user and using function, remove the duplicate and print the new list onto screen.

def rem_duplicate(list1):
    new=[]
    for item in list1:
        if item not in new:
            new.append(item)
            print(item)        
nums=[]
limit=int(input("enter limit:"))
for j in range(limit):
    item=int(input("enter item:"))
    nums.append(item)
rem_duplicate(nums)


        
    



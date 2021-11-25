#
def convert(l):
    new=[]
    for item in l:
        item=int(item)
        new.append(item)
    return new
nums=["12","23","34","45"]
x=convert(nums)
print(x)

#pass statement
def test():
    pass
var=int(input("enter a number:"))
print(var)

#calculator
def addition(x,y):
    return x+y
def substraction(x,y):    
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
def display():
    print("1.ADD\t2.SUB\t3.MUL\t4.DIV")
    opt=int(input("enter an option:"))
    return opt

n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
while True:
    option=display()
    
    if option==1:
        res=addition(n1,n2)
    if option==2:
        res=substraction(n1,n2)
    if option==3:
        res=multiplication(n1,n2)
    if option==4:
        res=division(n1,n2)
      

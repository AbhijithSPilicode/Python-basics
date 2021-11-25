#wap a function which wil taking atleast 2 parameters.if it is 2 values,sum it and return to function call
#else if user passes more values than that sum of all value should return
def add(x,y,*z):
    res=x+y
    if z!=():
        for i in z:
            res+=i
        return res
    else:
        return res

print(add(12,2))
print(add(12,2,3))
print(add(12,2,3,4))

#method2

def addition(a,b,c=0,d=0,e=0,f=0):
    return a+b+c+d+e+f
print(addition(12,2))
print(addition(12,2,3))
print(addition(12,2,3,4))

print("\n")        
#lambda function
(lambda x:print(x+10))(12)

print("\n")

    

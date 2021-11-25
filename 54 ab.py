#filter
a=[1,2,3,4,5,6,7,8,9,10]
b=filter(lambda x:x%2==0,a)
print(list(b))

#1.wap to get number type of list from user and print only multiple of 5
a=[1,2,3,4,5,6,7,8,9,10]
c=filter(lambda x:x%5==0,a)
print(list(c))
#2.wap to get a list of word & print word starting with "a"
words=["python","level","malayalam","stem","mom","dad","root","abhijith","apple"]
d=list(filter(lambda x:x.startswith("a"),words))
print(d)

#3.wap to get a list of letter and print palindrome
words=["python","level","malayalam","stem","mom","dad","root"]
s=list(filter(lambda x:x==x[::-1],words))
print(s)       

#4.wap to get number type of list from user and print only multiple of 3 which are greater than 30
nums=[12,23,33,45,60,90,66,56,55]
e=list(filter(lambda x:x%3==0 and x>30,nums))
print(e)

#5.wap to get number from user and print only integers
nums=[]
limit=int(input("how many item in list?:"))
for i in range(limit):
    inp=float(input("enter a number:"))
    nums.append(inp)
q=list(filter(lambda x:x.is_integer(),nums))
for i in q:
    print(i)

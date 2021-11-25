#palindrome using while
string=input("enter a string:").lower()
length=len(string)
var_1=0
while(var_1<length):
 pal=string[::-1]
 var_1=var_1+1
if(pal==string):
    print("palindrome")
else:
    print("not palindrome")

#method 2
string_1=input("enter a string:").lower()
var_2=0
rev=""
while var_2<=len(string_1)-1:
    rev=string_1[var_2]+rev
    var_2+=1
if string_1==rev:
    print(f" {string} is palindrome")
    


#reversing and palindrome of a number
num1=int(input("enter a number:"))
rev_2=0
while num1>0:
    rem1=num1%10
    rev_2=(rev_2*10)+rem1
    num=num/10
print(f"{rev_2}")  
if(rev_2==num1):
  print("palindrome")

#break
var_3=1
while var_3<=10:
    if var_3==8:
        break
    print(f"{var_3}-python")
    var_3=var_3+1
    
  

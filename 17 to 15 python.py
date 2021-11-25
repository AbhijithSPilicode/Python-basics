#palindrome
word=input("enter the word:").lower()
reverse=word[::-1]
if(word==reverse):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")



num_1=int(input("enter first number:"))
num_2=int(input("enter second number"))
if(num_1 > num_2):
    print(f"{num_1} is bigger")
else:
    print(f"{num_2} is bigger")

quantity_1=int(input("enter quantity number:"))
price=quantity_1 * 100
if price>1000:
    print("eligible for 10% discount")
    rate=price-(price * 0.1)
    print(f"the rate after discount is {rate}")
else:
    print(f"price is {price}")

salary_1=int(input("enter salary number:"))
experience_1=int(input("enter year of experience number:"))
if(experience_1 > 5):
    salary_2=salary_1 + ( salary_1 * (5/100))
    print(f"{salary_2}")
else:
    print(f"{salary_1}")

num_3=int(input("enter number:"))
if(num_3>0):
    print(f"{num_3}")
else:
    absolute=abs(num_3)
    print(f"{absolute}")

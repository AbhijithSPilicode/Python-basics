mark1=float(input('mark1:'))
mark2=float(input('mark2:'))
mark3=float(input('mark3:'))
avg=(mark1 + mark2 + mark3)/3
if avg>=90 and avg<=100:
     print(f"The grade is A+")
elif avg>=80 and avg<90:
    print(f"The grade is A")
elif avg>=70 and avg<80:
    print(f"The grade is B+")
elif avg>=60 and avg<70:
    print(f"The grade is B")
elif avg>=50 and avg<60:
    print(f"The grade is C+")
else:
    print(f"The grade is F")

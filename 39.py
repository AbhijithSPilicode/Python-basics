#removing repeated number in a list
numbers=[12,2,23,12,56,11,23,78,11]
new=[]
for item in numbers:
    if item not in new:
        new.append(item)
print(new)        

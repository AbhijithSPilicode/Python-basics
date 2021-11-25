Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#lisr
#list
fruit=["apple","orange","mango","grapes","kiwi","banana","watermelon","strawberry","pineapple"]
print(fruit)
['apple', 'orange', 'mango', 'grapes', 'kiwi', 'banana', 'watermelon', 'strawberry', 'pineapple']
#list is mutable
len(fruit)
9
fruit[0]
'apple'
fruit[7]="jackfruit"
fruit
['apple', 'orange', 'mango', 'grapes', 'kiwi', 'banana', 'watermelon', 'jackfruit', 'pineapple']
list1=[12,"stem",3.14,"a"]
list1[3]
'a'
print(list1 + [22.32,"root"])
[12, 'stem', 3.14, 'a', 22.32, 'root']
list2=[1,5,4,3]
list3=list1+list2
print(list3)
[12, 'stem', 3.14, 'a', 1, 5, 4, 3]
print(list2 *2)
[1, 5, 4, 3, 1, 5, 4, 3]

Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"dictionary"
'dictionary'
"key and value"
'key and value'
"use {} to denote"
'use {} to denote'
fruits={"apple":"red","banana":"yellow","dates":"black","watermelon":"green"}
fruits
{'apple': 'red', 'banana': 'yellow', 'dates': 'black', 'watermelon': 'green'}
fruits["watermelon"]
'green'
fruits["grapes"]="purple"
fruits
{'apple': 'red', 'banana': 'yellow', 'dates': 'black', 'watermelon': 'green', 'grapes': 'purple'}
"apple" in fruits
True
"  apple" in fruits
False
"apple" not in fruits
False
for fruit in fruits:
    print(fruit)

    
apple
banana
dates
watermelon
grapes
for fruit in fruits:
    print(fruit,"-",fruits[fruit])

    
apple - red
banana - yellow
dates - black
watermelon - green
grapes - purple
#you cannot have duplicate keys,but can have duplicate value.
dict1={12:12.234,"stem":12,34.67:(1,2,3,4),("python","programming"):[12,23,34,45],"test":{1:100,2:200,3:300}}
dict1[12]
12.234
dict1["stem"]
12
dict1[34.67]
(1, 2, 3, 4)
dict1[("python","programming")]
[12, 23, 34, 45]
dict1["test"]
{1: 100, 2: 200, 3: 300}
#nested datatype is above

===== RESTART: C:/Users/user/Desktop/asap/python/56 dictionary datatype.py =====
number of items:4
fruit:apple
color:red
fruit:lemon
color:yellow
fruit:grape
color:purple
fruit:orange
color:orange
{'apple': 'red', 'lemon': 'yellow', 'grape': 'purple', 'orange': 'orange'}
"$"
'$'
capitals={"kerala":"trivandrum","tamilnadu":"chennai","rajasthan":"jaipur","punjab":"chandigarh","goa":"panaji","andhrapradesh":"amaravathi","westbengal":"kolkata"}
a=capitals.copy()
a
{'kerala': 'trivandrum', 'tamilnadu': 'chennai', 'rajasthan': 'jaipur', 'punjab': 'chandigarh', 'goa': 'panaji', 'andhrapradesh': 'amaravathi', 'westbengal': 'kolkata'}
a[goa]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a[goa]
NameError: name 'goa' is not defined
a["goa"]
'panaji'
capitals.clear()
a.get("gujrat")
print(a.get("gujrat","invalid key"}}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
print(a.get("gujrat","invalid key"))
invalid key
print(a.get("punjab","invalid key"))
chandigarh
a.pop("goa") #remove item
'panaji'
a
{'kerala': 'trivandrum', 'tamilnadu': 'chennai', 'rajasthan': 'jaipur', 'punjab': 'chandigarh', 'andhrapradesh': 'amaravathi', 'westbengal': 'kolkata'}
a.pop("goa","invalid key")
'invalid key'
a.popitem()
('westbengal', 'kolkata')
a
{'kerala': 'trivandrum', 'tamilnadu': 'chennai', 'rajasthan': 'jaipur', 'punjab': 'chandigarh', 'andhrapradesh': 'amaravathi'}
#popitem remove the last item
capitals.keys()
dict_keys([])
a.keys
<built-in method keys of dict object at 0x03EE7528>
a.keys()
dict_keys(['kerala', 'tamilnadu', 'rajasthan', 'punjab', 'andhrapradesh'])
type(a.keys())
<class 'dict_keys'>
for i in a.keys():
    print(i)

    
kerala
tamilnadu
rajasthan
punjab
andhrapradesh
a.items()
dict_items([('kerala', 'trivandrum'), ('tamilnadu', 'chennai'), ('rajasthan', 'jaipur'), ('punjab', 'chandigarh'), ('andhrapradesh', 'amaravathi')])
for i in a.items():
    print(i)

    
('kerala', 'trivandrum')
('tamilnadu', 'chennai')
('rajasthan', 'jaipur')
('punjab', 'chandigarh')
('andhrapradesh', 'amaravathi')
for i,j in a.items():
    print(i,"-",j)

    
kerala - trivandrum
tamilnadu - chennai
rajasthan - jaipur
punjab - chandigarh
andhrapradesh - amaravathi
a.setdefault("karnataka")
a
{'kerala': 'trivandrum', 'tamilnadu': 'chennai', 'rajasthan': 'jaipur', 'punjab': 'chandigarh', 'andhrapradesh': 'amaravathi', 'karnataka': None}
a.setdefault("telengana","hyderabad")
'hyderabad'
a
{'kerala': 'trivandrum', 'tamilnadu': 'chennai', 'rajasthan': 'jaipur', 'punjab': 'chandigarh', 'andhrapradesh': 'amaravathi', 'karnataka': None, 'telengana': 'hyderabad'}
a.update({"gujrat":"gandhinagar"})
a
{'kerala': 'trivandrum', 'tamilnadu': 'chennai', 'rajasthan': 'jaipur', 'punjab': 'chandigarh', 'andhrapradesh': 'amaravathi', 'karnataka': None, 'telengana': 'hyderabad', 'gujrat': 'gandhinagar'}

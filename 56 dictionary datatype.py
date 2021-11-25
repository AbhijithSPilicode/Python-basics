#dictionary datatype
fruits={}
limit=int(input("number of items:"))
for i in range(limit):
          key=input("fruit:")
          value=input("color:")
          fruits[key]=value
print(fruits)

#
user={"abhijith":"xyz"}
username={}
limit1=int(input("number of items:"))
for i in range(limit1):
          key1=input("username:")
          if(key1 in user):
             print("acces granted") 
             value1=input("password:") 
             if(value1==user[key1]):
                 print("access granted")
             else:
                 print("password wrong")
             
          else:
              print("username is invalid")

        
    

        

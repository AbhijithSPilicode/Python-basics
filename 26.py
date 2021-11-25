#break
username="leomessi"
password="unstoppable"
count=0;
while True:
    if count<3:
        username1=input("enter user name:")
        count+=1
        if(username1==username): 
          password1=input("enter the password:")
          if password1== password:
            print("access granted")
            break
          else:
              print("password is incorrect")
              break
    else:
             print("username is incorrect")
             break

#continue - to skip a value in a loop

var=0
while var<=5:
    var+=1
    if var==3:
        continue
    print(var)
         


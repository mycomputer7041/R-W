

use=input("enter your user name :")
passs=input("enetr your password :")

if(use=="admin" and passs=="1234"):
    print("login succesfully")
elif(use!="admin" or passs!="1234"):    
    print("user name or password are incorrect")
else:
    print("retry aggin")

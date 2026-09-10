
print("old printing")
with open("sempal.txt","r") as file:
    oldp=file.read()
    print("old contant is a :",oldp)

with open("sempal.txt","w") as file:
    file.write("learning file handling in python is fun ")

print("the new pinting statment ")

with open("sempal.txt","r") as file:
    newp=file.read()
    print("new statment is a :",newp)

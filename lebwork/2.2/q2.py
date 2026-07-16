a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

if(a<b and a<c):
    print("the first number is minimum")
elif(b<c and b!=a and a!=c):
    print("the secound number is largest")
elif(c<b and b!=a):
    print("the third number is largest")
elif(a==b and b==c):
    print("all three numbers are equal")
elif(a==b):
    print("first and secound number is equal")
elif(b==c):
    print("second and third number is equal")
elif(a==c):
    print("first and third number is equal")
else:
    print("your number is invalid")
a=int(input("enter your age :"))

if(a<0):
    print("enter valid number ")
elif(a<=12):
    print("child")
elif(a<=19):
    print("teenager")
elif(a<=59):
    print("adult")
elif(a>=60):
    print("senior")
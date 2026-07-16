a=bool(input("enter the firstvalue :"))
b=bool(input("enter the second value:"))

if(a and b):
    print("both are true")
else:
    print("both are not true")
if(a or b):
    print("either one is true")
else:
    print("both are false")
if(not a):
    print("first value is false")
else:
    print("first value is true")
if(not b):
    print("second value is false")  
else:
    print("second value is true")       
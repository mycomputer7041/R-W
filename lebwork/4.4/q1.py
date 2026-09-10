b=int(input("enter your array size:"))
a=[0]*b
count=0
for i in range(b):
    a[i]=int(input("enter your number :"))
    count=count+1
print(a)
print("the array size is a :",count)
b=int(input("enter array  size:"))
a=[0]*b
sum=0
for i in range(b):
    a[i]=float(input("enter your value :"))
    sum=sum+a[i]

ave=sum/b
print("the average of all value is a :",ave)
    
a=[0]*6
for i in range(1,6):
    a[i]=int(input("enter your number :"))
print("all even number")
for i in range(1,6):
    if a[i]%2==0:
        print(a[i])

print("all odd number")
for i in range(1,6):        
    
    if a[i]%2!=0:
        print(a[i])

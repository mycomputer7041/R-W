a=int(input("enter your number :"))

b=[10,2,5,30,5,6]

for i in b:
    if i==a:
        print("number is found")
        print(b[i-1])
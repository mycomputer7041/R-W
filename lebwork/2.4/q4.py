a=int(input("enter your number :"))
j=0
i=0
for i in range(1,a+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    print()
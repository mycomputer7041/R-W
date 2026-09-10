a=int(input("enter array size:"))

b=[0]*a
c=[0]*a
t=[0]*a

for i in range(a):
    b[i]=int(input("enter your value array of A:"))
for i in range(a):
    c[i]=int(input("enter your value array of B:"))
for i in range(a):
    t[i]=b[i]+c[i]
    # print(t[i])
print(t)



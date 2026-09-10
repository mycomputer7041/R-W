a=[1,2,3,4,5]
b=int(input("eneter your removebel element  :"))

for i in a:
    if i==b:
        a.remove(b)
        print(a)

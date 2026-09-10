s=input("enter your world")
print("start with :", s.startswith("hello"))
print("wnd with :",s.endswith("world"))


m="Data123#Science!"
sum=""
for i in m:
    if i.isalpha():
        sum=sum+i
print("the aplfa bet deleted string is ",sum)
    


a="python"
rev=a[::-1]
print(rev)
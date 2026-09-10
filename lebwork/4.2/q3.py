def res(s):
    if len(s)==0:
        return s
    else:
        return res(s[1:])+s[0]

s=input("enter your string :")

result=res(s)
print(result)
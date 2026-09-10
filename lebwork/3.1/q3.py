a=input("enter user string value :")

b="".join(reversed(a))
print(b)

if(a==b):
    print("the string is pelindrome")
else:
    print("string are not palindrome")
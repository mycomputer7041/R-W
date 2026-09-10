try:
    a=[1,2,3,4]
    index=int(input("enter your index number :"))
    print(f"your index is a {a[index]}")
except IndexError:
    print("error: this index number is a not avelabel")
    


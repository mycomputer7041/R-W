a=int(input("enter your digits"))
count = 0
    
for i in range(100):
    if a > 0:
        count = count + 1
        a = a // 10  
    else:
        break

print("Total digits in your number:", count)
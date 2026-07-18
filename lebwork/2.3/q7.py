
for i in range(1,51):
    if(i%2==0 and i%3==0):
        print(i,"number devisibel by 2 and 3")
    elif(i%2==0):
        print(i,"number dividible by only 2")
    elif(i%3==0):
        print(i,"number divisible by only 3")
    else:
        print(i,"number not devisible by 2 or 3")
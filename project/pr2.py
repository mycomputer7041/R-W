while (True):
    print("""\n\tWelcom to the pattern generator and NUmber Analzer!

          Select an option:
          1.Ganret pattern
          2.Analyze a Range of Numbers
          3.Exit""")
    user=int(input("enter your number :"))

    if(user==1):
        n=int(input("enter your pattern lenth:"))
        for i in range(0,n):
            for j in range(1,i+2):
                print("*", end="")
            print()
    elif(user==2):
        a=int(input("enter your start number :"))
        b=int(input("enter your end number :"))
        sum=0
        for i in range(a,b):
            if(i%2==0):
                print(f"number {i} is even")
            else:
                print(f"number {i} is odd")
            
            sum=sum+i
        print("the total is a ",sum)

        
    elif(user==3):
        break
        print("you exit in this projects")
    else:
        print("please enter valied number in 1,2,3")

a=int(input("enter your year:"))

if(a%4==0 and a%100!=0):
    print("the year is a leap year")
elif(a%100==0 and a%400!=0):
    print("the year is not a leap year")    
elif(a%400==0 and a%100!=0):
    print("the year is a leap year")
else:
    print("the year is not a leap year")    

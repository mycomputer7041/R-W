a=int(input("enter temperature :"))

if(a>=40):
    print("the temperature is very hot")
elif(a>=30 and a<40):
    print("the temperature is hot")
elif(a>=20 and a<30):
    print("the temperature is normal")  
else:
    print("the temperature is cold")
    
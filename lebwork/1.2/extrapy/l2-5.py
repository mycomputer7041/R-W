a=int(input("enter student marks in 1 to 100:"))

if(a<0 or a>100):
    print("the student marks is invalid")
elif(a>=90):
    print("the student grade is A")
elif(a>=75):
    print("the student grade is B")
elif(a>=50):
    print("the student grade is C")
else:
    print("the student failed")

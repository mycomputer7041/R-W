class age:

    def getter(self,age):
        print("user age is a:",age)

    def setter(self,age):
        if(age>0):
            print("user can eligibel")
        else:
            print("invelied age ")

b1=age()
age=int(input("enter youe age :"))
b1.getter(age)
b1.setter(age)

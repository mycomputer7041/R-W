class bank:

    def __init__(self,name,accno,bal,pin):
        self.name=name
        self.accno=accno
        self.bal=bal
        self.pin=pin

    def withdraw(self,pinn,wamount):
        if pinn==self.pin and wamount<=self.bal:
            self.bal=self.bal-wamount

        else:
            print("invelid pin or amount")

    def diposit(self,damount):
        self.bal+=damount

    def display(self,pinn):
        if pinn==self.pin:
            self.bal=self.bal-wamount+damount
            print(f"\n\naccount holder name :{self.name}\naccount number :{self.accno}\naccount balance :{self.bal} ")


name=input("enter account holder name :")
accno=int(input("enter account number :"))
bal=int(input("enter account balance :"))
pin=int(input("input your 4 digit pin :"))
while (True):
    print("""1.withdraw amount
            2.deposit amount
            3.statment 
            4.exit """)
    ch=int(input("enter your choice"))
    person1=bank(name,accno,bal,pin)

    if ch==1:
        pinn=int(input("enter pin number :"))
        wamount=int(input("enter withdraw amount"))

        person1.withdraw(pinn,wamount)
    elif ch==2:
        damount=int(input("enter deposit amount"))
        person1.diposit(damount)
    elif ch==3:
        pinn=int(input("enter pin number :"))
        person1.display(pinn)
    else:
        break  






        
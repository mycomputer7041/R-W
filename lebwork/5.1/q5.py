class account:
    def __init__(self,bal):
        self.__balance=bal

    def deposit(self,amount):
        self.__balance+=amount
        print(amount,"amount added")

    def withdraw(self,amount):
        if(amount<=self.__balance):
        
            self.__balance-=amount
            print(amount,"amount withdraw ")
        else:
            print("enter vilid value")

    def display(self):
        print("total balens of account is :",self.__balance)


bal=int(input("enter your main account balance :"))
b1=account(bal)

amo=int(input("enter your deposit amount :"))
b1.deposit(amo)

ame=int(input("enter your withdraw amount"))
b1.withdraw(ame)

b1.display()


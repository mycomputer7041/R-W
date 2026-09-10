try:
    num1=float(input("enter first number :"))
    num2=float(input("enter second number :"))

    result=num1/num2
    print("result is a :",result)
except ZeroDivisionError:
    print("error : cna not divied by zero")
class employee:
    def __init__(self,name,age,empid,salary):
        self.name=name
        self.age=age
        self.__empid=empid
        self.__salary=salary

    def get_empid(self):
        return self.__empid
    def set_empid(self,empid):
        self.__empid=empid

    def get_salary(self):
        return self.__salary
    def set_selary(self,salary):
        self.__salary=salary

    def display(self):
        print(f"""name : {self.name}
        age : {self.age}
        empid : {self.get_empid()}
        salary :{self.get_salary()}""")
    def __del__(self):
        pass

class manager(employee):

    def __init__(self,name,age,empid,salary,dep):
        super().__init__(name,age,empid,salary)
        self.dep=dep

    def display(self):
        super().display()
        print(f"department : {self.dep}")
class devloper(employee):

    def __init__(self,name,age,empid,salary,plan):
        super().__init__(name,age,empid,salary)
        self.plan=plan

    def display(self):
        super().display()
        print(f"programing language :{self. plan}")

# name=input("enter your name :")
# age=input("enter your age :")
# empid=input("enter your id number :")
# salary=input("enter your salary :")


a = None
b = None
c = None
while (True):
    print(""" 1.create a person\n 2.create a employee\n 3.create a manager\n 4.show details\n 5.Exit """)
    ch=int(input("enter your choice :"))
    if(ch==1):
        name=input("enter your name :")
        age=input("enter your age :")
        empid=input("enter your id number :")
        salary=input("enter your salary :")
        a=employee(name,age,empid,salary)
       
    elif(ch==2):
        name=input("enter your name :")
        age=input("enter your age :")
        empid=input("enter your id number :")
        salary=input("enter your salary :")
        dep=input("enter your department :")
        b=manager(name,age,empid,salary,dep)
       
    elif(ch==3):
        name=input("enter your name :")
        age=input("enter your age :")
        empid=input("enter your id number :")
        salary=input("enter your salary :")
        plan=input("enter your programing language :")
        c=devloper(name,age,empid,salary,plan)
        
    elif(ch==4):
        if a: a.display()
        if b: b.display()
        if c: c.display()
    elif(ch==5):
            break 
    






        




    
        
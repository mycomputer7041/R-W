class Student:

    def __init__(self, name, roll_no, marks, gender, age):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.gender = gender
        self.age = age
        

    def show_info(self, password):

        if password == "friend":
            print("\n--- Student Details ---")
            print(f"Name   : {self.name}")
            print(f"Roll No: {self.roll_no}")
            print(f"Marks  : {self.marks}")
            print(f"Gender : {self.gender}")
            print(f"Age    : {self.age}")
        else:
            print("\n pass word are wrong")

    
    def update(self,rem):
        
        print(f"old marks is {self.marks}")
        self.marks = rem
        print(f"new updated marks is a {rem}")

        print("\n--- Student Updated Details ---")
        print(f"Name   : {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks  : {self.marks}")
        print(f"Gender : {self.gender}")
        print(f"Age    : {self.age}")

    def result(self):
    
            if self.marks>=35:
                print("sudent is passed")
            else:
                print("student is a fail")

    def friinfo(self,spass,namef,agef,gen):

        if spass=="krish":

            print(f"frind name is a :{namef}")
            print(f"age of friend :{agef}")
            print(f"gender is a :{gen}")
        else:

            print("your password is wrong")

    
        



s1 = Student("Rahul", 101, 85, "Male", 20)

user_pass = input("enter password : ")


s1.show_info(user_pass)


s1.update(45)
spass=input("enetr frind password : ")
s1.result()
s1.friinfo(spass,"krish",25,"male")
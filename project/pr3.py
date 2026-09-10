print("Welcome to the student data organizer!")
all_student=[]

while True:

    print(""" Select an option 
                1.Add Student
                2.Display All Student
                3.Updata All Information
                4.Delete Student
                5.Display Sublects offered
                6.Exit""")
    ch=int(input("enter your choice :"))

    if(ch==1):

        name=input("enetr student name :")
        id=int(input("enter student id :"))
        age=int(input("enter student age :"))
        dob=input("enter student dob:")
        grade=input("enter student grad:")
        sub=input("enter your all subject name:")

        
        sub_list = set([s.strip() for s in sub.split(",")])
       

        idtup=(id,dob)

        student1={
            "name":name,
            "idtup":idtup,
            "id":id,
            "dob":dob,
            "age":age,
            "grade":grade,   
            "sub":sub_list

        }

        all_student.append(student1)
        print("student add success fuuly")
    elif(ch==2):
        if (len(all_student)==0):
            print("no student data found")
        else:   
            for student1 in all_student:
                print(f"name:{student1['name']}")
                print(f"dob:{student1['dob']}")
                print(f"id:{student1['id']}")
                print(f"age:{student1['age']}")
                print(f"grade:{student1['grade']}")
                print(f"sub:{student1['sub']}")
                print("--"*50)
    elif(ch==3):
        if(len(all_student)==0):
            print("student not found")
        else:
            sid=int(input("enter your founding id"))
            found=False
            for student1 in all_student:
                if(student1['id']==sid):
                    found=True
                    print(f"name:{student1['name']}")    
                    print(f"age:{student1['age']}")
                    print(f"grade:{student1['grade']}")

                    nname=input("enter new name :")
                    nage=input("enter new age :")
                    ngrade=input("enter new gread :")

                    if(nname!=""):
                        student1['name']=nname
                    if(nage!=""):
                        student1['age']=nage
                    if(ngrade!=""):
                        student1['grade']=ngrade

                    print("data updated ")
                    break
    elif(ch==4):
        if(len(all_student)==0):
            print("student was not found")
        else:
            did=int(input("enter student id :"))
            found=False
            for studen1 in all_student:
                if(student1['id']==did):
                    all_student.remove(student1)      
                    found=True
                    print("student deleted")
                    break
    elif ch == 5:
        if len(all_student) == 0:
            print("no student data found")
        else:
            
            for student1 in all_student:
                print(f"ID: {student1['id']} | Name: {student1['name']} | Subjects: {student1['sub']}")


    elif(ch==6):
        break  


    
student={"name":"Alice","age":20,"gread":"A"}
print("the starting student data is a :",student)

print("student key is a :",student.keys())
print("student value is a :",student.values())

student["city"]="Delhi"
print("city added stduent data is a :",student)

student["age"]=21
print("updated age student data is a :",student)``

del student["gread"]    
print("deleted stduent gread key :",student)
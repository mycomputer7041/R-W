class car:
    _compny=None
    _modal=None
    _color=None

    def setData(self,cm,ml,fl):
        self._compny=cm
        self._modal=ml
        self._color=fl

    def getData(self):
        print(f"This is compny name {self._compny}")


car1=car()
car1.setData("Tata","nano","pink")
car1.getData()





class Employee:
    _name = None
    _emp_id = None
    _salary = None

    def setData(self, n, i, s):
        self._name = n
        self._emp_id = i
        self._salary = s

    def getData(self):
        print(f"Employee Name: {self._name}, ID: {self._emp_id}, Salary: {self._salary}")


# Employee 1
emp1 = Employee()
emp1.setData("Rahul", 101, 25000)
emp1.getData()

# Employee 2 
emp2 = Employee()
emp2.setData("Priya", 102, 35000)
emp2.getData()



class Student:
    _name = None
    _roll_no = None
    _marks = None

    def setData(self, n, r, m):
        self._name = n
        self._roll_no = r
        self._marks = m

    def getData(self):
        print(f"Student Name: {self._name}, Roll No: {self._roll_no}, Marks: {self._marks}")


# Student 1
s1 = Student()
s1.setData("Amit", 15, 85)
s1.getData()

# Student 2
s2 = Student()
s2.setData("Neha", 20, 92)
s2.getData()




class Mobile:
    _brand = None
    _ram = None
    _price = None

    def setData(self, b, r, p):
        self._brand = b
        self._ram = r
        self._price = p

    def getData(self):
        print(f"Mobile Brand: {self._brand}, RAM: {self._ram}GB, Price: {self._price}")


# Mobile 1
m1 = Mobile()
m1.setData("Samsung", 8, 20000)
m1.getData()

# Mobile 2
m2 = Mobile()
m2.setData("Apple", 6, 65000)
m2.getData()
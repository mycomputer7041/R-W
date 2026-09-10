class employee:
    """
    Base class that stores general information about an employee.
    Uses private attributes for empid and salary to enforce encapsulation.
    """

    def __init__(self, name, age, empid, salary):
        """
        Initializes basic employee details
        arguments: name, age, empid, salary
        returns: nothing
        """
        self.name = name
        self.age = age
        self.__empid = empid      # Private attribute
        self.__salary = salary    # Private attribute

    def get_empid(self):
        """
        Gets the private employee ID
        arguments: none
        returns: employee ID string/number
        """
        return self.__empid

    def set_empid(self, empid):
        """
        Updates the private employee ID
        arguments: new empid value
        returns: nothing
        """
        self.__empid = empid

    def get_salary(self):
        """
        Gets the private salary amount
        arguments: none
        returns: salary string/number
        """
        return self.__salary

    def set_selary(self, salary):
        """
        Updates the private salary amount
        arguments: new salary value
        returns: nothing
        """
        self.__salary = salary

    def display(self):
        """
        Prints basic employee details to the console
        arguments: none
        returns: nothing
        """
        print(f"""name : {self.name}
        age : {self.age}
        empid : {self.get_empid()}
        salary :{self.get_salary()}""")

    def __del__(self):
        """
        Destructor method called when object is deleted
        arguments: none
        returns: nothing
        """
        pass


class manager(employee):
    """
    Child class inheriting from employee.
    Adds a department attribute specific to managers.
    """

    def __init__(self, name, age, empid, salary, dep):
        """
        Initializes manager details using super() for base class attributes
        arguments: name, age, empid, salary, department name
        returns: nothing
        """
        super().__init__(name, age, empid, salary)
        self.dep = dep

    def display(self):
        """
        Prints base employee details along with department
        arguments: none
        returns: nothing
        """
        super().display()
        print(f"department : {self.dep}")


class devloper(employee):
    """
    Child class inheriting from employee.
    Adds a programming language attribute specific to developers.
    """

    def __init__(self, name, age, empid, salary, plan):
        """
        Initializes developer details using super() for base class attributes
        arguments: name, age, empid, salary, programming language
        returns: nothing
        """
        super().__init__(name, age, empid, salary)
        self.plan = plan

    def display(self):
        """
        Prints base employee details along with programming language
        arguments: none
        returns: nothing
        """
        super().display()
        print(f"programing language :{self.plan}")




# Variables to hold created objects
a = None
b = None
c = None

while (True):
    """
    Displays menu options to create and view different employee types
    """
    print(""" 1.create a person\n 2.create a employee\n 3.create a manager\n 4.show details\n 5.Exit """)
    ch = int(input("enter your choice :"))

    if(ch == 1):
        # Creates a basic employee instance
        name = input("enter your name :")
        age = input("enter your age :")
        empid = input("enter your id number :")
        salary = input("enter your salary :")
        a = employee(name, age, empid, salary)
       
    elif(ch == 2):
        # Creates a manager instance
        name = input("enter your name :")
        age = input("enter your age :")
        empid = input("enter your id number :")
        salary = input("enter your salary :")
        dep = input("enter your department :")
        b = manager(name, age, empid, salary, dep)
       
    elif(ch == 3):
        # Creates a developer instance
        name = input("enter your name :")
        age = input("enter your age :")
        empid = input("enter your id number :")
        salary = input("enter your salary :")
        plan = input("enter your programing language :")
        c = devloper(name, age, empid, salary, plan)
        
    elif(ch == 4):
        # Displays details of all created objects
        if a: a.display()
        if b: b.display()
        if c: c.display()

    elif(ch == 5):
        # Exits the application loop
        break






        




    
        
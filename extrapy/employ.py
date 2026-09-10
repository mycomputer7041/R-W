class Employee:
    def __init__(self, name, empId, salary):
        self.name = name
        self.empId=empId
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,new_salary):
        if(new_salary > 0):
            self.__salary = new_salary
        else:
            return "salary Must be greater than 0"

    def display_info(self):
        print(f"Name: {self.name} and EmployeeId: {self.empId} salary: {self.__salary}")

    def work(self):
        print(f"Name: {self.name} is Working....")

class Developer(Employee):
    def __init__(self,name, empId, salary, programming_language):
        super().__init__(name, empId, salary)
        self.programming_langauge = programming_language

    def work(self):
        print(f"{super().work()} on this Programming Language {self.programming_langauge}")

    def display_info(self):
        return super().display_info()

class manager(Employee):
    def __init__(self,name,empid,salary,team_size):
        super().__init__(name,empid,salary)
        self.team_size=team_size

    def work(self):
        print(f"The manager is managing a team of {self.team_size}people")

    def display_info(self):
        print("the team size is a ",self.team_size)
        return super().display_info()

class trainer:
    def __init__(self,expertise):
        self.expertise=expertise
    def conduct_training(self):
        print(f"Conducting training on {self.expertise}")

    def work(self):
        print("this will help later with MRO")

class seniordeveloper(Developer,trainer):

    def __init__(self,name,empid,salary,programming_language,expertise,years_of_experience):
        super().__init__(self,name,empid,salary,programming_language)
        super().__init__(self,expertise)
        self.years_of_experience = years_of_experience

    def work(self):
        print("senior level behaviour")

    def display_info(self):
        
        return super().display_info()
    
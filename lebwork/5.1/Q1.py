class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"name :{self.name} age : {self.age}")

c1=person("milan",12)
c1.display()

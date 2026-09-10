class counter:
    def __init__(self):
        self.count=0

    def incre(self):
        self.count+=1

    def display(self):
        print(self.count)

c1=counter()
c1.display()

c1.incre()
c1.display()
c1.display()


class brother:
    def __init__(self,name,age,qualification):
        self.name = name
        self.age = age
        self.qualification = qualification

    def displaydetails(self):
        print(self.name + "\n" + self.age + "\n" + self.qualification)


class sister:
    def __init__(self,name,age,qualification,height,weight):
        self.height = height
        self.weight = weight

        brother.__init__(self,name,age,qualification)

    def printdetails(self):
        print("name =", self.name)
        print("age =", self.age)
        print("qualification =", self.qualification)
        print("height =", self.height)
        print("weight =", self.weight)


x = sister("pradeep", "21", "engineering", "173cm", "65kg")

x.printdetails()



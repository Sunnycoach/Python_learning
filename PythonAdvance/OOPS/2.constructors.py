class myClass():

    #class variables
    name = "Sunny"
    age = 23

    #instance variables
    def __init__(self,name = name,age = age): #constructor with the parameter
        self.name = name
        self.age = age

    def func1(self):
        print(f"hello {self.name}")

    def func2(self):
        print(f"Hi {self.name}")
    

# obj = myClass("Khushi",24)
# obj.func1()
# # obj.func2()

objNew = myClass("xyj",26)
objNew.age = 24
print(f"{objNew.age} and {objNew.name}")

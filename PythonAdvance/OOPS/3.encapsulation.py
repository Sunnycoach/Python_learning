class myClass():

    #class variables
    name = "Sunny"
    age = 23
    country="India"

    #instance variables
    def __init__(self,name = name,age = age, country = country): #constructor with the parameter
        self.__name = name
        self._age = age
        self.__country = country

    def func1(self):
        print(f"hello {self.__name} & {self._age} & {self.__country}")

    def func2(self):
        print(f"Hi {self.name}")
    

# obj = myClass("abc",35)
objNew = myClass()
objNew._age = 24
objNew.__name = "abvd"
objNew.__country = "Bharat"
objNew.func1()

print(f"{objNew._age} and {objNew.__name} and {objNew.country}")

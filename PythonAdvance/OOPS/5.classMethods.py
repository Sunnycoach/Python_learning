class myClass():

    n = 100
    newValue = 120

    def __init__(self):
        print("I will automtically called method")

    def __str__(self):
        return "I am string"
    
    @classmethod
    def _instanceMethod(cls, newValue = newValue):
        cls.newValue = newValue
    
    @staticmethod
    def dummy():
        print("i am for testing only")

obj1 = myClass()
print(obj1)
# print(obj1.newValue)
# obj1._instanceMethod(200)
# print(obj1.newValue)
# obj2 = myClass()
# print(obj2.newValue)
# obj1.dummy()
# print(obj1.newValue)
# obj2 = myClass()
# obj2.instanceMethod()
# print(obj2.newValue)
# print(obj1.n)
# obj2 = myClass()
# obj2.n = 200
# print(obj2.n)
# print(obj1.n)
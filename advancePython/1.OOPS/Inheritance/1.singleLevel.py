class Company:

    companyName:str = "MSU"
    title:str = "Decision Scientist"

    def __init__(self,companyName:str = companyName):
        self.companyName:str = companyName
    
    def info(self):
        # print(f'{self.companyName}')
        return self.companyName

class Employee(Company):

    def __init__(self,name,companyName=None):
        self.name = name

        if companyName is None:
            self.companyName = Company.companyName
        else:
            self.companyName = companyName
    
    def employeeInfo(self):
        company = Company.info(self)
        print(f"{self.name} is working in {company}")

obj = Employee("Sunny")
obj.employeeInfo()
        


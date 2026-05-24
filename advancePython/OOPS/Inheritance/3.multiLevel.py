class Company:

    companyName: str = "MSU"
    title: str = "Decision Scientist"

    def __init__(self, companyName: str = companyName):
        self.companyName = companyName
    
    def info(self):
        print(f'{self.companyName}')
        return f"Company: {self.companyName}"

class Manager(Company):

    def __init__(self,managerName,companyName=None):
        self.managerName=managerName
        if companyName is None:
            self.companyName = Company.companyName
        else:
            self.companyName = companyName
    
    def info(self):
        company = Company.info(self)
        print(f"{self.managerName} is working in {company} as a manager")
        return f"Manager:{self.managerName}, {company}"

class Employee(Manager):

    def __init__(self, empName,managerName, companyName=None):

        self.empName = empName
        self.managerName = managerName

        if companyName is None:
            self.companyName = Company.companyName
        else:
            self.companyName = companyName
    
    def info(self):
        response = Manager.info(self)
        print(f"Employee: {self.empName}, {response}")


objEmp = Employee("Sunny","John")
objEmp.info()
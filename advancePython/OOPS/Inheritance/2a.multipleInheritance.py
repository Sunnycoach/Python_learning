class Company:

    companyName: str = "MSU"
    title: str = "Decision Scientist"

    def __init__(self, companyName: str = companyName):
        self.companyName = companyName
    
    def info(self):
        print(f'{self.companyName}')
        return self.companyName


class Employee(Company):

    def __init__(self, name, companyName=None):

        self.name = name

        if companyName is None:
            self.companyName = Company.companyName
        else:
            self.companyName = companyName
    
    def info(self):
        company = Company.info(self)
        print(f"{self.name} is working in {company}")

class Contractor(Company):

    def __init__(self, name, companyName=None):
        self.name = name
        if companyName is None:
            self.companyName = Company.companyName
        else:
            self.companyName = companyName
    
    def info(self):
        company = Company.info(self)
        print(f"{self.name} is working in {company} as a contractor")


# obj = Employee("Sunny")
# obj.info()

contractor_obj = Contractor("John")
contractor_obj.info()
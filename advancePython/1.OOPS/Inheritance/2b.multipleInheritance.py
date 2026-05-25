class company:

    companyName: str = "MSU"
    title: str = "Decision Scientist"

    def __init__(self, companyName: str = companyName):
        self.companyName = companyName
    
    def info(self):
        print(f'{self.companyName}')
        return f"Company: {self.companyName}"

class client():

    def __init__(self,clientName):
        self.clientName=clientName

    def info(self):
        print(f"client: {self.clientName}")
        return f"client: {self.clientName}"

class employee(company,client):

    def __init__(self, empName,clientName, companyName=None):

        self.empName = empName
        self.clientName = clientName

        if companyName is None:
            self.companyName = company.companyName
        else:
            self.companyName = companyName
    
    def info(self):
        company1 = company.info(self)
        client1 = client.info(self)
        print(f"Employee: {self.empName}, {company1}, {client1}")


obj = employee("Sunny","John")
obj.info()



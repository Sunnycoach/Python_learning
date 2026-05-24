class apiFetch():

    def fetch(self):
        print("Fetching data from API")
    
class dbFetch():

    def fetch(self):
        print("Fetching data from Database")

class datalakeFetch():

    def fetch(self):
        print("Fetching data from Datalake")

obj = apiFetch()
obj.fetch()   
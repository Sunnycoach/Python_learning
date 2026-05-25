import pandas as pd

class dataExtract:

    def __init__(self, filePath:str):
        self.filePath = filePath
    
    def readData(self,separator:str):
        df = pd.read_csv(self.filePath, sep=separator)
        return df.head(2)

obj = dataExtract("OOPS/datasets/products.csv")
print(obj.readData(","))

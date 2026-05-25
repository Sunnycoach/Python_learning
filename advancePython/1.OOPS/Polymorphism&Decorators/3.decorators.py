def pandasDecorator(fxn):

    def mainfunc(*args):
        response = fxn(*args)
        response.to_parquet("OOPS/Polymorphism&Decorators/test.parquet")
        print(response.head(1))
        return response
    return mainfunc

@pandasDecorator
def csvToParquet(filepath:str):
    import pandas as pd
    df = pd.read_csv("OOPS\datasets\products.csv")
    return df

response = csvToParquet("products.csv")
print(response.head())

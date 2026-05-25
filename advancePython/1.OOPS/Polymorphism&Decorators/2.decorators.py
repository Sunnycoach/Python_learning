def decorator(fxn):

    def mainfxn(*args):
        print("before calling")
        response = fxn(*args)
        print("after calling")
        return response
        
    return mainfxn

@decorator
def fetchData(url:str, path):
    return f"Data from {url} is stored in {path}"

response = fetchData("www.google.com", "C:/Users/abc/Desktop")
print(response)
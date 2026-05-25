import time
from concurrent.futures import ThreadPoolExecutor
 

def fetchData(url:str):

    print(f"Fetching data from {url}")
    time.sleep(5)
    print(f"Data fetched from {url}")
    return "data from " + url

urlList= ['url1', 'url2', 'url3','url4','url5']

results = []
with ThreadPoolExecutor(max_workers=len(urlList)) as executor:
    futures = executor.map(fetchData, urlList)
    results.extend(futures)

print(results)

import asyncio
import time

async def apiCall(url:str,delay:int=3):
    print("fetching", url)
    await asyncio.sleep(delay)
    print(f"Data fetching from {url}")

async def execution():
    await asyncio.sleep(6)
    print("Executing")

async def transformation():
    await asyncio.sleep(3)
    print("Transforming")

async def main():

    tasks = await asyncio.gather(
        apiCall("https://api1.com"),
        execution(),
        transformation(),
    )

    # tasks = [apiCall(url) for url in [("https://api1.com"), ("https://api2.com"), ("https://api3.com")]]
    # results = await asyncio.gather(*tasks)
    print("All API calls done")

asyncio.run(main())
import asyncio

async def apiCall(url:str,delay:int):
    print("fetching", url)
    await asyncio.sleep(delay)
    print(f"Data fetching from {url}")
    return f"{url} response"

async def main():

    # task = asyncio.gather(
    #     apiCall("https://api1.com"),
    #     apiCall("https://api2.com"),
    #     apiCall("https://api3.com")
    # )

    tasks = [apiCall(url, delay) for url, delay in [("https://api1.com", 3), ("https://api2.com", 1), ("https://api3.com", 3)]]
    results = await asyncio.gather(*tasks)
    print("All API calls done")

asyncio.run(main())
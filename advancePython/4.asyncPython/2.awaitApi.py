import asyncio

async def apiCall():
    await asyncio.sleep(3)
    print("Data fetched")
    return "API response"

async def execute():
    print("Executing")
    result = await apiCall()
    print("Done", result)

asyncio.run(execute())
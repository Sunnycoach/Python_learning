import asyncio
import time

async def main():
#the moment user write async infront of func, it will become coroutines (tasks serialization for async to keep thread busy)
    print("hi")
    await asyncio.sleep(3)
    print("hello")

asyncio.run(main())
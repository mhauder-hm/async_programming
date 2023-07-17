#############################################
# Example to execute tasks sequentally 
#############################################
import asyncio
import time

async def x(i: float):
    await asyncio.sleep(i)
    return i

async def main():
    print(f"started at {time.strftime('%X')}")
    for f in asyncio.as_completed([x(i) for i in range(10)]):
        print(await f)
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

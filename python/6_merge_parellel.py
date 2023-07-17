#############################################
# Example to merge parallel tasks
#############################################
import asyncio
import time

async def x(i: float):
    await asyncio.sleep(i)
    if i == 5:
           raise Exception("This is unavoidable")
    return i

async def main():
    print(f"started at {time.strftime('%X')}")
    tt1 = asyncio.create_task(x(1))
    tt2 = asyncio.create_task(x(5))
    tt3 = asyncio.create_task(x(10))
    tt4 = asyncio.create_task(x(15))
    tlist = [tt1, tt2, tt3, tt4]

    done, pending = await asyncio.wait(tlist, return_when="FIRST_COMPLETED")
    print(f"FIRST_COMPLETED at {time.strftime('%X')}")
    done, pending = await asyncio.wait(tlist, return_when="FIRST_EXCEPTION")
    print(f"FIRST_EXCEPTION at {time.strftime('%X')}")
    done, pending = await asyncio.wait(tlist, return_when="ALL_COMPLETED")
    print(f"ALL_COMPLETED at {time.strftime('%X')}")

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

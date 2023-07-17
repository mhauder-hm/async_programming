#############################################
# Example using Awaitable Object
#############################################
import asyncio
import time

async def provide_after(delay_sec: float, to_say: str):
    await asyncio.sleep(delay_sec)
    print(to_say + f" said at {time.strftime('%X')}")
    return to_say

async def main():
    print(f"started at {time.strftime('%X')}")
    await provide_after(3, "1st awaitable")
    await provide_after(3, "2nd awaitable")
    print(f"finished at {time.strftime('%X')}")
    await asyncio.sleep(2)  # just to have some gap
    t1 = asyncio.create_task(provide_after(3, "1st task"))
    t2 = asyncio.create_task(provide_after(3, "2nd task"))
    t3 = asyncio.create_task(provide_after(5, "3nd task"))
    t4 = asyncio.create_task(provide_after(10, "4nd task"))
    print(f"started at {time.strftime('%X')}")
    await t1
    await t2
    await t3
    await t4
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())


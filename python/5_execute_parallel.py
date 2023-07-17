#############################################
# Example with parallel Tasks
#############################################
import asyncio

async def trigger(t, id):
    s = await t
    print(s, id)

async def main():
    t = asyncio.create_task(asyncio.sleep(1, 'Hello'))
    for i in range(3):
        asyncio.create_task(trigger(t, i))
    await t

asyncio.run(main())


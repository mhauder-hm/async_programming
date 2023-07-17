#############################################
# Example asynchronous exceptions
#############################################
import asyncio

async def will_ex():
    raise Exception("This is unavoidable")

async def main():
    try:
        await asyncio.create_task(will_ex())
    except Exception as ex:
        print(ex)

asyncio.run(main())


#############################################
# Example using Awaitable Object
#############################################
import asyncio
import time

async def say_hello(sec):
  #time.sleep(sec)
  await asyncio.sleep(sec)
  print("Greetings from say hello!" + str(sec))

async def main():
    print("eins")
    await say_hello_aw
    print("zwei")
    await say_hello(1)
    t1 = asyncio.create_task(say_hello(2.5))
    t2 = asyncio.create_task(say_hello(1))
    print("drei")
    await t1
    await t2
    await test()

async def test():
  print("fünf")

say_hello_aw = say_hello(2.5)
asyncio.run(main())
print("99")

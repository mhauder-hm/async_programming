#############################################
# Example using async / await
#############################################
import asyncio
from aiofile import async_open

async def main():
  async with async_open("C:/Code/async_programming/python/assets/file.txt", 'r') as afp:
      line = await afp.read()
      print(line)

asyncio.run(main())
print("Erster!")


#############################################
# Example using callback
#############################################
import asyncio

def callback(f):
    print("Callback:")
    print(file_content)

async def open_nonblocking(file, mode):
    f = open(file, mode)
    global file_content 
    file_content = f.read()

async def parallel_task():
    print("Paralleler Task!")

async def main():
        read_file = asyncio.create_task(open_nonblocking("C:/Code/async_programming/python/assets/file.txt", 'r'))
        read_file.add_done_callback(callback)
        other_task = asyncio.create_task(parallel_task())
        await read_file
        await other_task

asyncio.run(main())

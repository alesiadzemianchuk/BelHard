import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(5)
    print('Bye')




asyncio.run(main())
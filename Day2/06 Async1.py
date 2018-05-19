import asyncio
import datetime
import random

@asyncio.coroutine
def display_date(num, loop):
    end_time = loop.time() + 50.0
    print(f"Loop {num} is starting")
    while True:
        print(f"Loop: {num} Time: {datetime.datetime.now()}")
        if(loop.time() + 1.0 >= end_time):
            break
        yield from asyncio.sleep(random.randint(0,5))

def main():
    loop = asyncio.get_event_loop()

    asyncio.ensure_future(display_date(1, loop))
    asyncio.ensure_future(display_date(2, loop))

    loop.run_forever()


if __name__ == '__main__':
    main()
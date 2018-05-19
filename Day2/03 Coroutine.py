def co1():
    print("Starting coroutine")
    while True:
        data = yield
        print(data)

def main():
    co = co1()
    next(co)
    print("Back in main")
    co.send("Hi there coroutine")
    print("Back in main again")


if __name__ == '__main__':
    main()
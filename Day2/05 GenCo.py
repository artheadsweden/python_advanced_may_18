def genco():
    data = yield "Hello"
    yield data

def main():
    gc = genco()
    print(next(gc))
    print(gc.send("World"))


if __name__ == '__main__':
    main()
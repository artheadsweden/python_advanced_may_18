def outer(f):
    def inner(name):
        return ">>>>" + f(name) + "<<<<"
    return inner


def greeting(name):
    return "Hi " + name


def try_it():
    print(greeting('Bob'))

def main():
    global greeting
    greeting = outer(greeting)
    print(greeting("Anna"))
    try_it()

if __name__ == '__main__':
    main()
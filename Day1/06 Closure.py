def outer(x):
    def inner(y):
        print(x, y)
    return inner

def func_fact(e):
    def inner(b):
        return b**e
    return inner

def main():
    f = outer(3)
    f(10)
    f2 = outer(5)
    f2(11)
    f(34)

    sq = func_fact(2)
    cu = func_fact(3)
    print(sq(4))
    print(cu(4))

    l = lambda x: lambda y: print(x, y)
    lf = l(33)
    lf(55)

if __name__ == '__main__':
    main()
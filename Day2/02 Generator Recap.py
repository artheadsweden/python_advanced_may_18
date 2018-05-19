def gen_func(n):
    i = 0
    while i < n:
        yield i
        i += 1


def non_gen_func(n):
    l = []
    i = 0
    while i < n:
        l.append(i)
        i += 1
    return l

def main():
    g = gen_func(3)
    print(next(g))
    print(next(g))
    print(next(g))

    ng = non_gen_func(3)
    print(ng)

    for x in gen_func(10):
        print(x)

    for n in (x**2 for x in range(10)):
        print(n)


if __name__ == '__main__':
    main()
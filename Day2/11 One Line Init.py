
class A:
    def __init__(self, a, b, c, d, e, f, g, h):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})




def main():
    a = A(1, 2, 3, 4, 5, 6, 7, 8)
    print(a.a)
    print(a.b)
    print(a.c)
    print(a.d)
    print(a.e)
    print(a.f)
    print(a.g)
    print(a.h)


if __name__ == '__main__':
    main()
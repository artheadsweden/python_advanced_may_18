from functools import partial

def pow(base, exp):
    return base**exp


def main():
    r = pow(2, 3)
    print(r)

    cube = partial(pow, exp=3)
    square = partial(pow, exp=2)
    print(cube(2))
    print(square(2))

if __name__ == '__main__':
    main()
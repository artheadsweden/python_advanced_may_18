def my_func(a, b, c):
    print(a, b, c)


def main():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_list = [10, 20, 30]

    my_func(*my_list)
    my_func(*my_dict)
    my_func(**my_dict)

    my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]
    a, *b, c = my_list2
    print(a, b, c)

if __name__ == '__main__':
    main()
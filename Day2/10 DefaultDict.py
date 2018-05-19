from collections import defaultdict

def main():
    text = "When I was a kid I always wanted a cat but all I got was a gold fish"
    my_counter = defaultdict(int)
    for c in text:
        my_counter[c] += 1
    print(sorted(my_counter.items()))


    my_normal_dict = {}
    for c in text:
        if c in my_normal_dict:
            my_normal_dict[c] += 1
        else:
            my_normal_dict[c] = 1
    print(sorted(my_normal_dict.items()))



if __name__ == '__main__':
    main()
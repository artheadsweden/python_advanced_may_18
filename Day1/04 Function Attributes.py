def function_object(n=0):
    private_value = n

    def func():
        print('private_value =', private_value)

    def increase_by(x):
        nonlocal private_value
        private_value += x

    def decrease_by(x):
        nonlocal private_value
        private_value -= x

    def get_value():
        return private_value

    def set_value(new_value):
        nonlocal private_value
        private_value = new_value

    func.increase_by = increase_by
    func.decrease_by = decrease_by
    func.getvalue = get_value
    func.set_value = set_value
    func.pv = private_value

    return func


def main():
    f = function_object(10)
    f()
    f.increase_by(2)
    f()
    print(f.pv)

if __name__ == '__main__':
    main()
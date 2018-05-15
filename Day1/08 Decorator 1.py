from functools import wraps

def signs(f):
    @wraps(f)
    def inner(*args, **kwargs):
        return ">>>>" + f(*args, **kwargs) + "<<<<"
    return inner

@signs
def greeting(name):
    return "Hi " + name

@signs
def advanced_greeting(greeting, name):
    return greeting + " " + name

@signs
def zero_args():
    return "Oh"

@signs
def bye(name):
    return "Bye " + name

def main():
    print(greeting('Alice'))
    print(greeting.__name__)
    print(bye("Alice"))
    print(advanced_greeting('Hello','Alice'))
    print(zero_args())



if __name__ == '__main__':
    main()
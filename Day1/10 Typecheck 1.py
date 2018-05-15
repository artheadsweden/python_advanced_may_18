from functools import wraps
from inspect import signature

def typeasserter(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func
        sig = signature(func)
        bound_types = sig.bind(*ty_args, **ty_kwargs).arguments
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs).arguments
            for name, value in bound_values.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(f"Argument {name} is {type(value)}. Expected {bound_types[name]}.")
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeasserter(int, str, float)
def try_me(a, b, c):
    print(a, b, c)


def main():
    try_me("4", "hi", 3.4)


if __name__ == '__main__':
    main()
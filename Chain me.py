def chain(init_val, functions):
    for i in functions:
        init_val = i(init_val)
    return init_val


def add10(x):
    return x + 10


def mul30(x):
    return x * 30


print(chain(10, [add10, mul30, mul30]))

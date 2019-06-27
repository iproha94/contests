import os


def _f(a):
    s = 0
    for c in str(a):
        s += int(c)

    while s % 4 != 0:
        a += 1
        s = 0
        for c in str(a):
            s += int(c)

    return a


def f(a):
    return _f(a)


if os.environ.get('DEBUG', False):
    print(f"{f(432)} = 435")
    print(f"{f(99)} = 103")
    print(f"{f(237)} = 237")
    print(f"{f(42)} = 44")
else:
    print(f(int(input())))

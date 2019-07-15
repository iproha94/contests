import os


def _f(n, x):
    return x * 2


def f(n, x):
    return _f(n, x)


if os.environ.get('DEBUG', False):
    print(f"{f(3, 1)} = 2")
    print(f"{f(4, 2)} = 4")
    print(f"{f(69, 6)} = 12")
else:
    T = int(input())
    for _ in range(T):
        n, x = list(map(int, input().split()))
        print(f(n, x))

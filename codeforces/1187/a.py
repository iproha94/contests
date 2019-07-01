import os


def _f(n, s, t):
    x = s + t - n
    os = s - x
    ot = t - x
    return max(os, ot) + 1


def f(n, s, t):
    return _f(n, s, t)


if os.environ.get('DEBUG', False):
    print(f"{f(10, 5, 7)} = 6")
    print(f"{f(10, 10, 10)} = 1")
    print(f"{f(2, 1, 1)} = 2")
else:
    for _ in range(int(input())):
        n, s, t = list(map(int, input().split()))
        print(f(n, s, t))

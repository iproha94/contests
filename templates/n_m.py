import os


def _f(n, m):
    return 0


def f(n, m):
    return _f(n, m)


if os.environ.get('DEBUG', False):
    print(f"{f(0, 0)} = 0")
else:
    n, m = list(map(int, input().split()))
    print(f(n, m))

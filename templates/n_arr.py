import os


def _f(n, arr):
    return 0


def f(n, arr):
    return _f(n, arr)


if os.environ.get('DEBUG', False):
    print(f"{f(0, [])} = 0")
else:
    n = int(input())
    arr = list(map(int, input().split()))
    print(f(n, arr))

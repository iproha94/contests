import os


def f(arr):
    return 0


if os.environ.get('DEBUG', False):
    print(f"{f([])} = 0")
else:
    input()
    arr = list(map(int, input().split()))
    print(f(arr))

import os


def _f(a, b, c):
    return 2 * c + min(a, b) * 2 + (1 if a != b else 0)


def f(a, b, c):
    return _f(a, b, c)


if os.environ.get('DEBUG', False):
    print(f"{f(1, 1, 1)} = 4")
    print(f"{f(2, 1, 2)} = 7")
    print(f"{f(3, 5, 2)} = 11")
    print(f"{f(2, 2, 1)} = 6")
    print(f"{f(1000000000, 1000000000, 1000000000)} = 4000000000")
else:
    a, b, c = list(map(int, input().split()))
    print(f(a, b, c))

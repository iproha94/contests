import os


def _f(k, n, a, b):
    if b * n >= k:
        return -1

    if n * a < k:
        return n

    r = (k - b * n) / (a - b)
    if r == int(r):
        r = int(r) - 1
    else:
        r = int(r)

    if r < 0:
        return -1
    else:
        return r


def f(k, n, a, b):
    return _f(k, n, a, b)


if os.environ.get('DEBUG', False):
    print(f"{f(15, 5, 3, 2)} = 4")
    print(f"{f(15, 5, 4, 3)} = -1")
    print(f"{f(15, 5, 2, 1)} = 5")
    print(f"{f(15, 5, 5, 1)} = 2")
    print(f"{f(16, 7, 5, 2)} = 0")
    print(f"{f(20, 5, 7, 3)} = 1")
else:
    q = int(input())
    for i in range(q):
        k, n, a, b = list(map(int, input().split()))
        print(f(k, n, a, b))

import os


def _f(k, n, arr):
    v = 0
    p = 0
    for i in range(n):
        if arr[i] % 6 == 0 and arr[i] % 9 == 0:
            if v != 0:
                v -= 1
            if p != 0:
                p -= 1
        elif arr[i] % 6 == 0:
            v += 1
        elif arr[i] % 9 == 0:
            p += 1
        if k == v:
            return 'Vasya'
        elif k == p:
            return 'Petya'

    if v == p:
        return 'Draw'
    elif v > p:
        return 'Vasya'
    else:
        return 'Petya'


def f(k, n, arr):
    return _f(k, n, arr)


if os.environ.get('DEBUG', False):
    print(f"{f(2, 10, [6, 9, 54, 6, 54, 9, 9, 1, 2, 3])} = Petya")
    print(f"{f(2, 6, [54, 6, 6, 9, 9, 9])} = Vasya")
else:
    k, n = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(f(k, n, arr))

import os


def _f(n, b, a, arr):
    max_a = a
    for i in range(n):
        if a == 0 and b == 0:
            return i
        elif arr[i] == 1:
            if a == max_a:
                a -= 1
            elif b > 0:
                b -= 1
                a += 1
            else:
                a -= 1
        else:
            if a > 0:
                a -= 1
            else:
                b -= 1

    return n


def f(n, b, a, arr):
    return _f(n, b, a, arr)


if os.environ.get('DEBUG', False):
    print(f"{f(5, 2, 1, [0, 1, 0, 1, 0])} = 5")
    print(f"{f(6, 2, 1, [1, 0, 0, 1, 0, 1])} = 3")
else:
    n, b, a = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(f(n, b, a, arr))

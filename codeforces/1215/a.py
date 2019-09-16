import os


def f_min(a1, a2, k1, k2, n):
    n -= a1 * (k1 - 1)
    n -= a2 * (k2 - 1)
    return n if n > 0 else 0


def f_max(a1, a2, k1, k2, n):
    if k1 > k2:
        k1, k2 = k2, k1
        a1, a2 = a2, a1

    d = a1 * k1
    if n >= d:
        n -= d
        del1 = a1
    else:
        del1 = n // k1
        n -= del1 * k1

    d = a2 * k2
    if n >= d:
        n -= d
        del2 = a2
    else:
        del2 = n // k2
        n -= del2 * k2

    return del1 + del2


def f(a1, a2, k1, k2, n):
    return f"{f_min(a1, a2, k1, k2, n)} {f_max(a1, a2, k1, k2, n)}"


if os.environ.get('DEBUG', False):
    print(f"{f(2, 3, 5, 1, 8)} = 0 4")
    print(f"{f(3, 1, 6, 7, 25)} = 4 4")
    print(f"{f(6, 4, 9, 10, 89)} = 5 9")
else:
    print(f(int(input()), int(input()), int(input()), int(input()), int(input())))

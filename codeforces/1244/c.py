import os


from math import gcd
from functools import reduce


def f(n, p, w, d):
    if n * w < p:
        return -1

    GCD = reduce(gcd, [n, p, w, d])
    n //= GCD
    p //= GCD
    w //= GCD
    d //= GCD

    z_min = int(n - p / d) - 1
    z_min = z_min if z_min > 0 else 0
    for z in range(z_min, n + 1):
        fx = (p - d * (n - z)) / (w - d)
        x = int(fx)
        if x != fx or x < 0:
            continue
        y = n - x - z

        if y >= 0:
            x_r = x * GCD
            y_r = y * GCD
            z_r = z * GCD
        else:
            x_r = (x + y) * GCD
            y_r = 0
            z_r = z * GCD

        if x_r * w + y_r * d == p:
            return f"{x_r} {y_r} {z_r}"


    return -1


if os.environ.get('DEBUG', False):
    print(f"{f(30, 60, 3, 1)} = 17 9 4")
    print(f"{f(10, 51, 5, 4)} = -1")
    print(f"{f(20, 0, 15, 5)} = 0 0 20")
    print(f"{f(20000, 0, 15000, 5000)} = 0 0 20000")
    print(f"{f(1, 2, 2, 1)} = 1 0 0")
    print(f"{f(1, 1, 2, 1)} = 0 1 0")
    print(f"{f(1, 3, 2, 1)} = -1")
    print(f"{f(130, 360, 4, 2)} = 90 0 40")
else:
    n, p, w, d = list(map(int, input().split()))
    print(f(n, p, w, d))

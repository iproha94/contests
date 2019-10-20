import os


def f(a, b, c, d, k):
    c1 = a // c
    if a % c:
        c1 += 1

    c2 = b // d
    if b % d:
        c2 += 1

    if c1 + c2 > k:
        return -1
    else:
        return f"{c1} {c2}"


if os.environ.get('DEBUG', False):
    print(f"{f(7, 5, 4, 5, 8)} = 7 1")
    print(f"{f(7, 5, 4, 5, 2)} = -1")
    print(f"{f(20, 53, 45, 26, 4)} = 1 3")
else:
    t = int(input())
    for _ in range(t):
        a, b, c, d, k = list(map(int, input().split()))
        print(f(a, b, c, d, k))

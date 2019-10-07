import os


def f(n):
    if n == 2:
        return 2
    else:
        return n % 2


if os.environ.get('DEBUG', False):
    print(f"{f(2)} = 2")
    print(f"{f(5)} = 1")
    print(f"{f(8)} = 0")
    print(f"{f(11)} = 1")
else:
    q = int(input())
    for _ in range(q):
        print(f(int(input())))

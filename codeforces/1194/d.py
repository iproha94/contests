import os
import random


def _f(n, k):
    if n == 0:
        return 'Bob'
    elif n == 1:
        return 'Alice'
    elif n == 2:
        return 'Alice'

    q = [None] * (n + 1)
    q[0] = False
    q[1] = True
    q[2] = True

    for i in range(3, n + 1):
        if k > i:
            q[i] = not q[i-1] or not q[i-2]
        else:
            q[i] = not q[i-1] or not q[i-2] or not q[i-k]

    # print(q)
    return 'Alice' if q[-1] else 'Bob'


def f(n, k):
    return _f(n, k)


if os.environ.get('DEBUG', False):
    print(f"{f(0, 3)} = Bob")
    print(f"{f(3, 3)} = Alice")
    print(f"{f(3, 4)} = Bob")
    print(f"{f(4, 4)} = Alice")
    # print(f"{f(20, 4)} = ?")
else:
    T = int(input())
    for _ in range(T):
        n, k = list(map(int, input().split()))
        print(f(n, k))

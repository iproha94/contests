import os
import bisect 


def _f(n, x, k, t_arr):
    t_arr = list(set(t_arr))
    t_arr.sort()
    step = 1
    while step < k:
        r = t_arr.pop(0)
        try:
            t_arr.index(r + x)
        except ValueError:
            bisect.insort(t_arr, r + x)
        step += 1

    return t_arr[0]


def f(n, x, k, t_arr):
    return _f(n, x, k, t_arr)


if os.environ.get('DEBUG', False):
    print(f"{f(6, 5, 2, [1, 12, 13, 14, 15, 16])} = 6")
    print(f"{f(6, 5, 10, [1, 2, 3, 4, 5, 6])} = 10")
    print(f"{f(5, 7, 12, [5, 22, 17, 13, 8])} = 27")
else:
    n, x, k = list(map(int, input().split()))
    t_arr = list(map(int, input().split()))
    print(f(n, x, k, t_arr))

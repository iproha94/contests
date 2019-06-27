import os


def _f(n, k, a_arr):
    a_arr.sort()
    if a_arr[-1] - a_arr[0] > 2 * k:
        return -1
    return a_arr[0] + k


def f(n, k, a_arr):
    return _f(n, k, a_arr)


if os.environ.get('DEBUG', False):
    print(f"{f(5, 1, [1, 1, 2, 3, 1])} = 2")
    print(f"{f(4, 2, [6, 4, 8, 5])} = 6")
    print(f"{f(2, 2, [1, 6])} = -1")
    print(f"{f(3, 5, [5, 2, 5])} = 7")
else:
    q = int(input())
    for i in range(q):
        n, k = list(map(int, input().split()))
        a_arr = list(map(int, input().split()))
        print(f(n, k, a_arr))

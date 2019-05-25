import os


def _f(n, arr):
    a1 = None
    a2 = None
    a3 = None
    for a in arr:
        if a1 is None:
            a1 = a
        elif a2 is None and a != a1:
            a2 = a
        elif a3 is None and a != a1 and a != a2:
            a3 = a

    a_arr = []
    if a1 is not None:
        a_arr.append(a1)
    if a2 is not None:
        a_arr.append(a2)
    if a3 is not None:
        a_arr.append(a3)
    a_arr.sort()
    if len(a_arr) == 3:
        if a_arr[1] - a_arr[0] == a_arr[2] - a_arr[1]:
            return a_arr[1] - a_arr[0]
        else:
            return -1
    elif len(a_arr) == 2:
        d = a_arr[1] - a_arr[0]
        if d % 2 == 0:
            return int(d / 2)
        else:
            return d
    else:
        return 0


def f(n, arr):
    return _f(n, arr)


if os.environ.get('DEBUG', False):
    print(f"{f(6, [1, 4, 4, 7, 4, 1])} = 3")
    print(f"{f(5, [2, 2, 5, 2, 5])} = 3")
    print(f"{f(4, [1, 3, 3, 7])} = -1")
    print(f"{f(2, [2, 8])} = 3")
    print(f"{f(2, [2, 9])} = 7")
    print(f"{f(3, [1, 1, 1])} = 0")
else:
    n = int(input())
    arr = list(map(int, input().split()))
    print(f(n, arr))
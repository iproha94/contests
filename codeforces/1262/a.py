import os


def f(arr):
    min_r = arr[0][1]
    max_l = arr[-1][0]
    for l, r in arr:
        min_r = min(min_r, r)
        max_l = max(max_l, l)

    if max_l >= min_r:
        return max_l - min_r
    else:
        return 0


if os.environ.get('DEBUG', False):
    print(f"{f([[4, 5], [5, 9], [7, 7]])} = 2")
    print(f"{f([[11, 19], [4, 17], [16, 16], [3, 12], [14, 17]])} = 4")
    print(f"{f([[1, 10]])} = 0")
    print(f"{f([[1, 1]])} = 0")
else:
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        for _ in range(n):
            arr.append(list(map(int, input().split())))
        print(f(arr))

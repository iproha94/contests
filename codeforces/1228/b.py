import os


def f(r_arr, c_arr):
    result = 1
    for i, r in enumerate(r_arr):
        vars = 1
        for j in range(r):
            if c_arr[j] == i:
                return 0

        if r < len(c_arr) and c_arr[r] > i:
            return 0

        for j in range(r + 1, len(c_arr)):
            if c_arr[j] < i:
                vars *= 2
            else:
                vars *= 1

        result *= vars
        result %= 1000000007

    return result


if os.environ.get('DEBUG', False):
    print(f"{f([0, 3, 1], [0, 2, 3, 0])} = 2")
    print(f"{f([0],[1])} = 0")
    print(f"{f([16, 16, 16, 16, 15, 15, 0, 5, 0, 4, 9, 9, 1, 4, 4, 0, 8, 16, 12], [6, 12, 19, 15, 8, 6, 19, 19, 14, 6, 9, 16, 10, 11, 15, 4])} = 797922655")
else:
    list(map(int, input().split()))
    r_arr = list(map(int, input().split()))
    c_arr = list(map(int, input().split()))
    print(f(r_arr, c_arr))

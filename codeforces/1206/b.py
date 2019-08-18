import os


def f(arr):
    n_1 = 0
    n_0 = 0
    n_m1 = 0

    r = 0

    for a in arr:
        if a > 1:
            n_1 += 1
            r += (a - 1)
        elif a == 1:
            n_1 += 1
        elif a == 0:
            n_0 += 1
        elif a == -1:
            n_m1 += 1
        elif a < -1:
            r += (-a - 1)
            n_m1 += 1
        else:
            raise ValueError()

    if n_m1 % 2 != 0 and n_0 == 0:
        return r + n_0 + 2
    else:
        return r + n_0


if os.environ.get('DEBUG', False):
    print(f"{f([-1, 1])} = 2")
    print(f"{f([-2, 0, 2])} = 3")
    print(f"{f([0, 0, 0, 0])} = 4")
    print(f"{f([-5, -3, 5, 3, 0])} = 13")
else:
    n = int(input())
    arr = list(map(int, input().split()))
    print(f(arr))

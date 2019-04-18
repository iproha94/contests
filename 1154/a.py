import os


def _f(x1, x2, x3, x4):
    x_arr = [x1, x2, x3, x4]
    x_arr.sort(reverse=True)
    c = x_arr[0] - x_arr[1]
    a = x_arr[2] - c
    b = x_arr[3] - c
    return a, b, c


def f(x1, x2, x3, x4):
    a, b, c = _f(x1, x2, x3, x4)
    return f"{a} {b} {c}"


if os.environ.get('DEBUG', False):
    print(f"{f(3, 6, 5, 4)} = 2 1 3")
    print(f"{f(40, 40, 40, 60)} = 20 20 20")
    print(f"{f(201, 101, 101, 200)} = 1 100 100")
else:
    x1, x2, x3, x4 = list(map(int, input().split()))
    print(f(x1, x2, x3, x4))

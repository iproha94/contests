import os


def f(a_arr):
    return 0


if os.environ.get('DEBUG', False):
    print(f"{f([3, 1, 6, 6, 3, 1, 1])} = 2")
    print(f"{f([1, 1, 4, 4, 4, 7, 8, 8])} = 0")
    print(f"{f([4, 2, 5, 2, 6, 2, 7])} = 1")
else:
    q = int(input())
    for _ in range(q):
        print(f(list(map(int, input().split()))))

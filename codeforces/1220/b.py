import os
import math


def f(matr):
    result = [0] * len(matr)
    result[0] = int(math.sqrt(matr[0][1] * matr[0][2] / matr[1][2]))
    for i in range(1, len(matr)):
        result[i] = int(matr[i][i - 1] / result[i - 1])

    return "".join(str(e) + ' ' for e in result)


if os.environ.get('DEBUG', False):
    print(f"{f([[0, 4, 6, 2, 4], [4, 0, 6, 2, 4], [6, 6, 0, 3, 6], [2, 2, 3, 0, 2], [4, 4, 6, 2, 0]])} = 2 2 3 1 2 ")
    print(f"{f([[0, 99990000, 99970002], [99990000, 0, 99980000], [99970002, 99980000, 0]])} = 9999 10000 9998 ")
else:
    n = int(input())
    print(f([list(map(int, input().split())) for _ in range(n)]))

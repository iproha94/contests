import os


def is_flag(p, j1, i1, j2, i2):
    if (j2 + 1 - j1) % 3 != 0:
        return False

    step = (j2 + 1 - j1) // 3

    c1 = p[j1][i1]
    for j in range(j1, j1 + step):
        for i in range(i1, i2 + 1):
            if p[j][i] != c1:
                return False

    c2 = p[j1 + step][i1]
    if c1 == c2:
        return False
    for j in range(j1 + step, j1 + 2 * step):
        for i in range(i1, i2 + 1):
            if p[j][i] != c2:
                return False

    c3 = p[j1 + 2 * step][i1]
    if c3 == c2:
        return False
    for j in range(j1 + 2 * step, j1 + 3 * step):
        for i in range(i1, i2 + 1):
            if p[j][i] != c3:
                return False

    return True


# print(is_flag(['a','a','b','b','a','a'], 0, 0, 5, 0))

def _f(n, m, p, j1, i1, j2, i2):
    if is_flag(p, j1, i1, j2, i2):
        return 1 + _f(n, m, p, j1, i1, j2, i2 + 1) + \
               _f(n, m, p, j1, i1 + 1, j2, i2 + 1) + \
               _f(n, m, p, j2 + 1, i1, j2 + 1 + (), i2)
    else:
        return _f(n, m, p, j1, i1, j2, i2)


def f(n, m, p):
    return _f(n, m, p, 0, 0, 2, 0)


if os.environ.get('DEBUG', False):
    print(f"{f(4, 3, [['aaa'],['bbb'], ['ccb'], ['ddd']])} = 6")
    print(f"{f(6, 1, ['a','a','b','b','c','c'])} = 1")
else:
    n, m = list(map(int, input().split()))
    p = []
    for i in range(n):
        p.append(input())
    print(f(n, m, p))

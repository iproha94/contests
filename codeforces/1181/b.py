import os


def _f(l, n):
    sn = str(n)
    i1 = l // 2 - int(not (l % 2)) 
    i2 = l // 2

    r1 = None
    while i1 >= 0 and sn[i1 + 1] == '0':
        i1 -= 1
    if i1 >= 0:
        r1 = int(sn[:i1 + 1]) + int(sn[i1 + 1:])

    r2 = None
    while i2 < l and sn[i2] == '0':
        i2 += 1
    if i2 < l:
        r2 = int(sn[0:i2]) + int(sn[i2:])

    if r1 and r2:
        return min(r1, r2)
    else:
        return r1 if r1 else r2


def f(l, n):
    return _f(l, n)


if os.environ.get('DEBUG', False):
    print(f"{f(2, 11)} = 2")

    print(f"{f(6, 110000)} = 10001")
    print(f"{f(4, 1234)} = 46")
    print(f"{f(4, 1204)} = 124")
    print(f"{f(5, 10101)} = 111")
    print(f"{f(5, 12345)} = 168")
    print(f"{f(7, 1234567)} = 1801")
    print(f"{f(3, 101)} = 11")
else:
    l = int(input())
    n = int(input())
    print(f(l, n))

import os


def _f(x, y, z):
    if x + y < z:
        return (0, 0)
    else:
        ost1 = x % z
        ost2 = y % z
        if (z - ost1) <= ost2 or (z - ost2) <= ost1:
            if (z - ost1) <= (z - ost2):
                return x // z + y // z + 1, (z - ost1)
            else:
                return x // z + y // z + 1, (z - ost2)
        else:
            return x // z + y // z, 0


def f(x, y, z):
    return ''.join(str(e) + ' ' for e in _f(x, y, z))


if os.environ.get('DEBUG', False):
    print(f"{f(5, 4, 3)} = 3 1")
    print(f"{f(6, 8, 2)} = 7 0")
    print(f"{f(6, 8, 1)} = 14 0")
    print(f"{f(5, 5, 5)} = 2 0")
    print(f"{f(3, 1, 5)} = 0 0")
    print(f"{f(3, 2, 5)} = 1 2")
    print(f"{f(7, 5, 5)} = 2 0")
    print(f"{f(7, 4, 5)} = 2 1")
else:
    x, y, z = list(map(int, input().split()))
    print(f(x, y, z))

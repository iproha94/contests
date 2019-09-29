import os


def dif_dig(i):
    si = sorted(str(i))
    for j in range(1, len(si)):
        if si[j] == si[j - 1]:
            return False

    return True


def f(l, r):
    i = l
    while i <= r:
        if dif_dig(i):
            return i

        i += 1

    return -1


if os.environ.get('DEBUG', False):
    print(f"{f(121, 130)} = 123")
    print(f"{f(98766, 100000)} = -1")
else:
    l, r = list(map(int, input().split()))
    print(f(l, r))

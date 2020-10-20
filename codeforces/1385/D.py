from math import log2

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def f(s):
    if len(s) == 1:
        return int(s != 'a')

    n = int(log2(len(s)))
    t = {}
    for i in range(n):
        t[alphabet[i]] = [0] * 2 ** (i + 1)

    t[alphabet[n]] = [0] * len(t[alphabet[n - 1]])

    for i, c in enumerate(s):
        ord_c = ord(c)
        if ord_c > ord(alphabet[n]):
            continue
        if c == alphabet[n]:
            ord_c -= 1
        t[c][i // int(len(s) / 2 ** (ord_c - 96))] += 1

    for c in range(n):
        print(alphabet[c])
    return 0


if __name__ == "__main__":
    for _ in range(int(input())):
        input()
        print(f(input()))

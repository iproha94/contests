import os


def _f(n, arr):
    t_n = [0] * (n + 1)
    for a in arr:
        t_n[a] += 1

    t_n.sort(reverse=True)

    k = None
    for i in range(1, n):
        if t_n[i] >= t_n[i - 1]:
            t_n[i] = t_n[i - 1] - 1
        if t_n[i] <= 0:
            t_n[i] = 0
            k = i
            break

    if k is None:
        return sum(t_n)
    else:
        s = 0
        i = 0
        while i < k:
            s += t_n[i]
            i += 1

        return s


def f(n, arr):
    return _f(n, arr)


if os.environ.get('DEBUG', False):
    print(f"{f(6, [1, 2, 2, 3, 3, 3])} = 6")
    print(f"{f(8, [1, 4, 8, 4, 5, 6 ,3, 8])} = 3")
    print(f"{f(16, [2, 1, 3, 3, 4 ,3 ,4 ,4, 1, 3, 2, 2, 2, 4, 1, 1])} = 10")
    print(f"{f(9, [2, 2, 4, 4, 4, 7, 7, 7, 7])} = 9")
else:
    q = int(input())
    for _ in range(q):
        n = int(input())
        arr = list(map(int, input().split()))
        print(f(n, arr))

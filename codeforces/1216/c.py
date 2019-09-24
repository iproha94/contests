import os


def foo(w, b):
    if b[0] <= w[0] and b[1] < w[1]: #LN 0-1
        if b[2] >= w[2] and b[3] > w[1] and b[3] < w[3]: #PV 13-14
            w[1] = b[3]
            return w
        elif b[2] > w[0] and b[2] < w[2] and b[3] == w[3]: #PV 17
            w[2] = b[2]
            return w
        elif b[2] >= w[2] and b[3] == w[3]: #PV 18-19
            return None
        elif b[2] > w[0] and b[2] < w[2] and b[3] > w[3]: #PV 22
            w[2] = b[2]
            return w
        elif b[2] >= w[2] and b[3] > w[3]: #PV 23-24
            return None
        else:
            return w
    elif b[0] > w[0] and b[0] < w[2] and b[1] < w[1]: #LN 2
        if b[2] >= w[2] and b[3] > w[1] and b[3] < w[3]:  # PV 13-14
            return w
        elif b[2] > w[0] and b[2] < w[2] and b[3] == w[3]:  # PV 17
            return w
        elif b[2] >= w[2] and b[3] == w[3]:  # PV 18-19
            w[0] = b[0]
            return w
        elif b[2] > w[0] and b[2] < w[2] and b[3] > w[3]:  # PV 22
            return w
        elif b[2] >= w[2] and b[3] > w[3]:  # PV 23-24
            w[0] = b[0]
            return w
        else:
            return w
    elif b[0] <= w[0] and b[1] == w[1]: #LN 5-6
        if b[2] >= w[2] and b[3] > w[1] and b[3] < w[3]:  # PV 13-14
            w[1] = b[3]
            return w
        elif b[2] > w[0] and b[2] < w[2] and b[3] == w[3]:  # PV 17
            w[2] = b[2]
            return w
        elif b[2] >= w[2] and b[3] == w[3]:  # PV 18-19
            return None
        elif b[2] > w[0] and b[2] < w[2] and b[3] > w[3]:  # PV 22
            w[2] = b[2]
            return w
        elif b[2] >= w[2] and b[3] > w[3]:  # PV 23-24
            return None
        else:
            return w
    elif b[0] > w[0] and b[0] < w[2] and b[1] == w[1]: #LN 7
        if b[2] >= w[2] and b[3] > w[1] and b[3] < w[3]:  # PV 13-14
            return w
        elif b[2] > w[0] and b[2] < w[2] and b[3] == w[3]:  # PV 17
            return w
        elif b[2] >= w[2] and b[3] == w[3]:  # PV 18-19
            w[0] = b[0]
            return w
        elif b[2] > w[0] and b[2] < w[2] and b[3] > w[3]:  # PV 22
            return w
        elif b[2] >= w[2] and b[3] > w[3]:  # PV 23-24
            w[0] = b[0]
            return w
        else:
            return w
    elif b[0] <= w[0] and b[1] > w[1] and b[1] < w[3]: #LN 10-11
        if b[2] >= w[2] and b[3] > w[1] and b[3] < w[3]:  # PV 13-14
            return w
        elif b[2] > w[0] and b[2] < w[2] and b[3] == w[3]:  # PV 17
            return w
        elif b[2] >= w[2] and b[3] == w[3]:  # PV 18-19
            w[0] = b[0]
            return w
        elif b[2] > w[0] and b[2] < w[2] and b[3] > w[3]:  # PV 22
            return w
        elif b[2] >= w[2] and b[3] > w[3]:  # PV 23-24
            w[0] = b[0]
            return w
        else:
            return w
    else:
        return 2


def f(w, b1, b2):
    w = foo(w, b1)
    if w is None:
        return "YES"
    else:
        return "YES" if foo(w, b2) is None else "NO"


if os.environ.get('DEBUG', False):
    print(f"{f([2, 2, 4, 4], [1, 1, 3, 5], [3, 1, 5, 5])} = NO")
    print(f"{f([3, 3, 7, 5], [0, 0, 4, 6], [0, 0, 7, 4])} = YES")
    print(f"{f([5, 2, 10, 5], [3, 1, 7, 6], [8, 1, 11, 7])} = YES")
    print(f"{f([0, 0, 1000000, 1000000], [0, 0, 499999, 1000000], [500000, 0, 1000000, 1000000])} = YES")
else:
    w = list(map(int, input().split()))
    b1 = list(map(int, input().split()))
    b2 = list(map(int, input().split()))
    print(f(w, b1, b2))

import os


def _f(n, m, t_l_r_arr):
    t_l_r_arr.sort(key=lambda x: (x[1], x[2]))

    for i in range(1, len(t_l_r_arr)):
        if t_l_r_arr[i - 1][0] != t_l_r_arr[i][0] and (
                t_l_r_arr[i - 1][2] > t_l_r_arr[i][1]
        ):
            return False, []

    r_arr = [None] * n
    last = 1
    for t, l, r in t_l_r_arr:
        for i in range(l - 1, r):
            if r_arr[i] is None:
                if i == 0 or r_arr[i - 1] is None:
                    r_arr[i] = last + (t - 1)
                    last = r_arr[i]
                else:
                    r_arr[i] = r_arr[i - 1] + (t - 1)
                    last = r_arr[i]

    m = None
    i = 0
    while m is None:
        m = r_arr[i]
        i += 1

    i = 0
    while r_arr[i] is None:
        r_arr[i] = m
        i += 1

    m = r_arr[0]
    for i in range(1, len(r_arr)):
        if r_arr[i] is None:
            r_arr[i] = r_arr[i - 1]
        m = min(m, r_arr[i])

    if m < 1:
        for i in range(len(r_arr)):
            r_arr[i] += (-m + 1)

    return True, r_arr


def f(n, m, t_l_r_arr):
    r, r_arr = _f(n, m, t_l_r_arr)
    if r:
        return "YES\n" + ''.join(str(e) + ' ' for e in r_arr)
    else:
        return "NO"


if os.environ.get('DEBUG', False):
    print(f"{f(7, 4, [[1, 1, 3], [1, 2, 5], [0, 5, 6], [1, 6, 7]])} = 1 2 2 3 5 4 4")
    print(f"{f(4, 2, [[1, 1, 4], [0, 2, 3]])} = NO")
    print(f"{f(6, 2, [[1, 1, 2], [0, 5, 6]])} = YES")
    print(f"{f(6, 2, [[1, 3, 4], [1, 5, 6]])} = YES")
    print(f"{f(6, 3, [[1, 2, 4], [0, 3, 5], [1, 4, 6]])} = NO")
else:
    n, m = list(map(int, input().split()))
    t_l_r_arr = []
    for _ in range(m):
        t_l_r_arr.append(list(map(int, input().split())))
    print(f(n, m, t_l_r_arr))
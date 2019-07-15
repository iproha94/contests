import os



def _f(n, m, matr):
    c_matr = []
    for i in range(n):
        c_matr.append(matr[i].count('*'))

    c_matr_t = [0] * m
    for i in range(n):
        for j in range(m):
            c_matr_t[j] += int(matr[i][j] == '*')

    max_w = 0
    for i in range(n):
        max_w = max(c_matr[i], max_w)

    w_arr = []
    for i in range(n):
        if c_matr[i] == max_w:
            w_arr.append(i)

    max_h = 0
    for i in range(m):
        max_h = max(c_matr_t[i], max_h)

    h_arr = []
    for i in range(m):
        if c_matr_t[i] == max_h:
            h_arr.append(i)

    f = False
    for i in w_arr:
        for j in h_arr:
            if matr[i][j] == '.':
                f = True
                break
        if f:
            break

    return n - max_h + m - max_w - int(f)


def f(n, m, matr):
    return _f(n, m, matr)


if os.environ.get('DEBUG', False):
    pass
    # print(f"{f(3, 1)} = 2")
    # print(f"{f(4, 2)} = 4")
    # print(f"{f(69, 6)} = 12")
else:
    q = int(input())
    for _ in range(q):
        n, m = list(map(int, input().split()))
        matr = []
        for i in range(n):
            matr.append(input())

        print(f(n, m, matr))

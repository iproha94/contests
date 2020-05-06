
def f(w, h, a, b, xld_yld_xru_yru_arr):
    m = [[None for _ in range(h + 2)] for _ in range(w + 2)]

    for i in range(h + 2):
        m[w + 1][i] = (0, 0)

    for i in range(w + 2):
        m[i][h + 1] = (0, 0)

    for xld, yld, xru, yru in xld_yld_xru_yru_arr:
        for i in range(xld, xru):
            for j in range(yld, yru):
                m[i][j] = (0, 0)

    for i in reversed(range(w + 1)):
        for j in reversed(range(h + 1)):
            if m[i][j] is None:
                m[i][j] = (m[i + 1][j][0] + 1, m[i][j + 1][1] + 1)

    for i in range(w + 1):
        for j in range(h + 1):
            f = True
            for k in range(a):
                if m[i + k][j][1] < b:
                    f = False
                    break
            if f:
                return f"{i} {j} {i + a} {j + b}"


if __name__ == "__main__":
    w, h, a, b = tuple(map(int, input().split()))
    xld_yld_xru_yru_arr = [tuple(map(int, input().split())) for _ in range(int(input()))]
    print(f(w, h, a, b, xld_yld_xru_yru_arr))

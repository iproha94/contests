import os


def f(n, m, q, Q):
    dc = []
    for i in range(n):
        dc.append([0, m, []])
    # print(dc)
    result = []

    mx_i_t = []
    for i in range(n):
        mx_i_t.append(True)

    for e in Q:
        if e[0] == 'D':
            _, d, s = e.split(' ')
            d = int(d) - 1
            s = int(s) - 1
            if s not in dc[d][2]:
                dc[d][2].append(s)
                dc[d][1] -= 1
                #
                mx_i_t[d] = False
        elif e[0] == 'R':
            _, d = e.split(' ')
            d = int(d) - 1
            dc[d][0] += 1
            dc[d][1] = m
            dc[d][2] = []

            mx_i_t[d] = True
        elif e[4] == 'A':
            first = -1
            for i in range(n):
                if mx_i_t[i]:
                    first = i
                    break
            if first != -1:
                result.append(mx_i_t[first])
            else:
                mx = dc[0][0] * dc[0][1]
                result.append(0)
                for i in range(len(dc)):
                    if mx < dc[i][0] * dc[i][1]:
                        mx = dc[i][0] * dc[i][1]
                        result[-1] = i
            result[-1] += 1
        else:  # e[4] == 'I'
            mn = dc[0][0] * dc[0][1]
            result.append(0)
            for i in range(len(dc)):
                if mn > dc[i][0] * dc[i][1]:
                    mn = dc[i][0] * dc[i][1]
                    result[-1] = i
                if mn == 0:
                    break
            result[-1] += 1
    return result


if os.getenv('TEST_MODE', False):
    print("------TEST MODE------")
    Q1 = [
        "DISABLE 1 2",
        "DISABLE 2 1",
        "DISABLE 3 3",
        "GETMAX",
        "RESET 1",
        "RESET 2",
        "DISABLE 1 2",
        "DISABLE 1 3",
        "DISABLE 2 2",
        "GETMAX",
        "RESET 3",
        "GETMIN",
    ]
    print(f'{f(3, 3, 12, Q1)} = [1, 2, 1]\n')

    Q2 = [
        "DISABLE 1 1",
        "DISABLE 2 2",
        "RESET 2",
        "DISABLE 2 1",
        "DISABLE 2 3",
        "RESET 1",
        "GETMAX",
        "DISABLE 2 1",
        "GETMIN",
    ]
    print(f'{f(2, 3, 9, Q2)} = [1, 2]\n')

    print("---------------------")
elif __name__ == "__main__":
    n, m, q = tuple(map(int, input().split()))
    Q = []
    for _ in range(q):
        Q.append(input())
    print("".join(str(e) + '\n' for e in f(n, m, q, Q)))


def f(n, m, A, B):
    s_w_a = []
    s_w_b = []

    for i in range(n):
        s_w_a.append(0)
        s_w_b.append(0)
        for j in range(m):
            s_w_a[-1] += A[i][j]
            s_w_b[-1] += B[i][j]
    # print(s_w_a)
    # print(s_w_b)

    s_h_a = []
    s_h_b = []
    for i in range(m):
        s_h_a.append(0)
        s_h_b.append(0)
        for j in range(n):
            s_h_a[-1] += A[j][i]
            s_h_b[-1] += B[j][i]
    # print(s_h_a)
    # print(s_h_b)

    for i in range(len(s_w_a)):
        if (s_w_a[i] - s_w_b[i]) % 2 != 0:
            return "No"
    for i in range(len(s_h_a)):
        if (s_h_a[i] - s_h_b[i]) % 2 != 0:
            return "No"

    return "Yes"


# print(f"{f(3, 3, [[0, 1, 0], [0, 1, 0], [1, 0, 0]], [[1, 0, 0], [1, 0, 0], [1, 0, 0]])} = Yes")
# print(f"{f(6, 7, [[0, 0, 1, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 1]], [[1, 1, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 0, 0], [1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 0, 1, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0, 1]])} = Yes")
# print(f"{f(3, 4, [[0, 1, 0, 1],[1, 0, 1, 0],[0, 1, 0, 1]],[[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1]])} = No")
# 
n, m = list(map(int, input().split()))
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
B = []
for i in range(n):
    B.append(list(map(int, input().split())))
print(f(n, m, A, B))

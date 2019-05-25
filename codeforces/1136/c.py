
def f(n, m, a_matr, b_matr):
    for i in range(n + m - 1):
        set_a = set()
        set_b = set()
        if i < n:
            for j in range(min(i + 1, m)):
                set_a.add(a_matr[i - j][j])
                set_b.add(b_matr[i - j][j])
        else:
            for j in range(i - n + 1, m):
                set_a.add(a_matr[n-1][j])
                set_b.add(b_matr[n-1][j])
        if set_a != set_b:
            return "NO"

    return "YES"


# print(f"{f(2, 2, [[1, 1], [6, 1]], [[1, 6], [1, 1]])} = YES")
# print(f"{f(2, 2, [[4, 4], [4, 5]], [[5, 4], [4, 4]])} = NO")
# print(f"{f(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 7], [2, 5, 6], [3, 8, 9]])} = YES")
# 
n, m = list(map(int, input().split()))
a_matr = []
for i in range(n):
    a_matr.append(list(map(int, input().split())))
b_matr = []
for i in range(n):
    b_matr.append(list(map(int, input().split())))
print(f(n, m, a_matr, b_matr))
# 
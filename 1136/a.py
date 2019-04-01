
def f(n, l_r_arr, k):
    now = 0
    for i in range(n):
        if l_r_arr[i][0] <= k <= l_r_arr[i][1]:
            now = i
            break
    return n - now


# print(f"{f(3, [(1, 3), (4, 7), (8, 11)], 2)} = 3")
# print(f"{f(3, [(1, 4), (5, 9), (10, 12)], 9)} = 2")
# print(f"{f(3, [(1, 4), (5, 9), (10, 12)], 1)} = 3")
# print(f"{f(3, [(1, 4), (5, 9), (10, 12)], 12)} = 1")
# print(f"{f(3, [(1, 1), (2, 2), (3, 3)], 1)} = 3")
# print(f"{f(3, [(1, 1), (2, 2), (3, 3)], 2)} = 2")
# print(f"{f(3, [(1, 1), (2, 2), (3, 3)], 3)} = 1")
# print(f"{f(1, [(1, 7),], 4)} = 1")
# print(f"{f(3, [(1, 3),(4, 5),(6, 7),], 4)} = 2")
# 
n = int(input())
l_r_arr = []
for i in range(n):
    l_r_arr.append(list(map(int, input().split())))
k = int(input())
print(f(n, l_r_arr, k))
# 
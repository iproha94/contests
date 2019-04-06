
def f(n, arr):
    a_min_mix = {}
    for i in range(n):
        if a_min_mix.get(arr[i], False) is False:
            a_min_mix[arr[i]] = [i, i]
        else:
            a_min_mix[arr[i]][1] = i

    min_mix = []
    for v in a_min_mix:
        min_mix.append(a_min_mix[v])

    rez = 0
    for i in range(len(min_mix)):
        for j in range(i + 1, len(min_mix)):
            rez = max(rez, min_mix[i][1] - min_mix[j][0])
            rez = max(rez, min_mix[j][1] - min_mix[i][0])
    return rez
# 
# 
# print(f"{f(5, [1, 2, 3, 2, 3])} = 4")
# print(f"{f(3, [1, 2, 1])} = 1")
# print(f"{f(7, [1, 1, 3, 1, 1, 1, 1])} = 4")
# print(f"{f(7, [1, 3, 1, 1, 1, 1, 1])} = 5")
# print(f"{f(3, [1, 1, 3])} = 2")
# 
n = int(input())
arr = list(map(int, input().split()))
print(f(n, arr))
# 
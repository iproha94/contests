
def f(n, s_arr, q, l_k_arr):
    s_arr.sort()
    s_arr = list(dict.fromkeys(s_arr))
    all_rez = []
    for l, k in l_k_arr:
        diap = []
        diap.append([s_arr[0] + l, s_arr[0] + k])
        for i in range(1, len(s_arr)):
            d1 = l + s_arr[i]
            d2 = k + s_arr[i]
            if diap[-1][0] <= d1 and diap[-1][1] >= d1:
                if d2 > diap[-1][1]:
                    diap[-1][1] = d2
            else:
                diap.append([d1, d2])
        rez = 0
        for d1, d2 in diap:
            rez += (d2 - d1 + 1)
        all_rez.append(rez)

    return ''.join(str(e) + ' ' for e in all_rez)


# print(f"{f(6, [3, 1, 4, 1, 5, 9], 3, [(7, 7), (0, 2), (8, 17)])} = 5 10 18")
# print(f"{f(2, [1, 500000000000000000], 2, [(1000000000000000000, 1000000000000000000), (0, 1000000000000000000)])} = 2 1500000000000000000")
# 
n = int(input())
s_arr = list(map(int, input().split()))
q = int(input())
l_k_arr = []
for i in range(q):
    l_k_arr.append(list(map(int, input().split())))
print(f"{f(n, s_arr, q, l_k_arr)}")
# 
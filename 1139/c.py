
def f(n, k, u_v_x_arr):
    u_v_x_map = []
    for i in range(n):
        u_v_x_map.append([])

    for u_v_x in u_v_x_arr:
        u_v_x_map[u_v_x[0] - 1].append((u_v_x[1] - 1, u_v_x[2]))
        u_v_x_map[u_v_x[1] - 1].append((u_v_x[0] - 1, u_v_x[2]))

    last_good_pathes = [0] * n
    last_all_pathes = [1] * n

    for j in range(n):
        for v_x in u_v_x_map[j]:
            last_all_pathes[j] += 1
            if v_x[1] == 1:
                last_good_pathes[j] += 1

    print(last_good_pathes)
    print(last_all_pathes)
    print("-------")

    for i in range(3, k + 1):
        good_pathes = [0] * n
        all_pathes = last_all_pathes.copy()

        for j in range(n):
            for v_x in u_v_x_map[j]:
                all_pathes[j] += last_all_pathes[v_x[0]]
                if v_x[1] == 0:
                    good_pathes[j] += last_good_pathes[v_x[0]]
                else:
                    good_pathes[j] += last_all_pathes[v_x[0]]

        last_good_pathes = good_pathes
        last_all_pathes = all_pathes

        print(last_good_pathes)
        print(last_all_pathes)
        print("-------")

    return sum(last_good_pathes)


# print(f"{f(7, 2, [[1, 2, 0], [2, 4, 0], [2, 6, 0], [3, 6, 1], [3, 7, 0], [5, 6, 1]])} = 4")
# print(f"{f(7, 3, [[1, 2, 0], [2, 4, 0], [2, 6, 0], [3, 6, 1], [3, 7, 0], [5, 6, 1]])} = X")
print(f"{f(4, 4, [[1, 2, 1], [2, 3, 1], [3, 4, 1]])} = 252")
# print(f"{f(4, 6, [[1, 2, 0], [1, 3, 0], [1, 4, 0]])} = 0")
# print(f"{f(3, 5, [[1, 2, 1], [2, 3, 0]])} = 210")

# n, k = list(map(int, input().split()))
# u_v_x_arr = []
# for i in range(n - 1):
#     u_v_x_arr.append(list(map(int, input().split())))
# print(f(n, k, u_v_x_arr))
# 
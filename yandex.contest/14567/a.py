import os


def f(n, m, pairs, k, capacity_count_arr):
    groups = []
    if m > 0:
        groups.append({pairs[0][0], pairs[0][1]})

    for i in range(1, len(pairs)):
        one_group = []
        for j in range(len(groups)):
            for member in groups[j]:
                if member == pairs[i][0] or member == pairs[i][1]:
                    one_group.append(j)
                    break

        if one_group:
            groups[one_group[0]] |= {pairs[i][0], pairs[i][1]}
            for j in range(len(one_group) - 1, 0, -1):
                groups[one_group[0]] |= groups.pop(one_group[j])
        else:
            groups.append({pairs[i][0], pairs[i][1]})

    for i in range(n):
        exist = False
        for group in groups:
            for member in group:
                if member == i:
                    exist = True
                    break
            if exist:
                break

        if not exist:
            groups.append([i])

    capacity_count_arr.sort(key=lambda x: (-x[0], -x[1]))
    groups.sort(key=lambda x: -len(x))

    for group in groups:
        if len(capacity_count_arr) == 0:
            return 0

        if len(group) <= capacity_count_arr[0][0] and capacity_count_arr[0][1] > 0:
            capacity_count_arr[0][1] -= 1
            if capacity_count_arr[0][1] == 0:
                capacity_count_arr.pop(0)
        else:
            return 0

    return 1


if os.environ.get('DEBUG', False):
    print(f"{f(6, 3, [(0, 1), (1, 2), (4, 5)], 2, [[3, 2], [5, 1]])} = 1")
    print(f"{f(6, 0, [], 1, [[0, 5]])} = 0")
    print(f"{f(6, 0, [], 1, [[1, 6]])} = 1")
    print(f"{f(6, 0, [], 1, [[0, 6]])} = 0")
    print(f"{f(3, 2, [(0, 1), (1, 2)], 1, [[2, 2],])} = 0")
else:
    n = int(input())
    m = int(input())
    pairs = []
    for _ in range(m):
        pairs.append(list(map(int, input().split())))
    k = int(input())
    capacity_count_arr = []
    for _ in range(k):
        capacity_count_arr.append(list(map(int, input().split())))
    print(f(n, m, pairs, k, capacity_count_arr))

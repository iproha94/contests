import os


def f(_, gens, __, s1_s2_cost_arr):
    a_b_c_lines = []
    for (s1, s2, cost) in s1_s2_cost_arr:
        s1 -= 1
        s2 -= 1
        if gens[s1] > gens[s2]:
            s1, s2 = s2, s1

        if cost < gens[s2]:
            a_b_c_lines.append([s1, s2, cost])

    a_b_c_lines.sort(key=lambda x: x[2])

    num_cost_result_lines_gens = []
    for (i, cost) in enumerate(gens):
        num_cost_result_lines_gens.append([i, cost, -1, []])
    num_cost_result_lines_gens.sort(key=lambda x: (x[1], x[0]))

    cost = 0
    while True:
        i = 0
        while i < len(num_cost_result_lines_gens) and \
                num_cost_result_lines_gens[i][2] != -1:
            i += 1

        if i == len(num_cost_result_lines_gens):
            break

        num_cost_result_lines_gens[i][2] = 1

        j = 0
        while j < len(num_cost_result_lines_gens) and \
                num_cost_result_lines_gens[j][2] != -1:
            j += 1

        if j == len(num_cost_result_lines_gens):
            break

        active_gens = []
        active_gens.append(i)
        while active_gens:
            i_j = active_gens.pop(0)

            for l, (a, b, c) in enumerate(a_b_c_lines):
                if num_cost_result_lines_gens[i_j][0] in [a, b]:
                    num_cost_result_lines_gens[i_j][3].append(l)

            k = 0
            while k < len(num_cost_result_lines_gens[i_j][3]) and \
                    a_b_c_lines[num_cost_result_lines_gens[i_j][3][k]][2] < num_cost_result_lines_gens[j][1]:
                l = 0
                while l < len(num_cost_result_lines_gens):
                    if num_cost_result_lines_gens[l][0] in [
                        a_b_c_lines[num_cost_result_lines_gens[i_j][3][k]][0],
                        a_b_c_lines[num_cost_result_lines_gens[i_j][3][k]][1]
                    ] and num_cost_result_lines_gens[l][2] == -1:
                        num_cost_result_lines_gens[l][2] = 0
                        cost += a_b_c_lines[num_cost_result_lines_gens[i_j][3][k]][2]
                        active_gens.append(l)
                    l += 1
                k += 1

    for x in num_cost_result_lines_gens:
        if x[2] == 1:
            cost += x[1]

    return cost


if os.environ.get('DEBUG', False):
    print(f"{f(3, [10, 50, 10], 2, [[1, 2, 5], [2, 3, 49]])} = 25")
    print(f"{f(5, [10, 1000, 1000, 11, 10], 4, [[1, 2, 1], [2, 3, 100], [3, 4, 1], [4, 5, 2]])} = 24")
    print(f"{f(1, [77,], 0, [])} = 77")
    print(f"{f(2, [11, 29], 1, [[1, 2, 17],])} = 28")
    print(f"{f(1, [11], 0, [])} = 11")
    print(f"{f(0, [], 0, [])} = 0")
else:
    n = int(input())
    gens = list(map(int, input().split()))
    c = int(input())
    s1_s2_cost_arr = []
    for _ in range(c):
        s1_s2_cost_arr.append(list(map(int, input().split())))
    print(f(n, gens, c, s1_s2_cost_arr))


def f(n, m, streets):
    houses_1 = []
    for i in range(n):
        houses_1.append([])
        for j in range(m):
            houses_1[i].append([streets[i][j], j, 0, 0])

        houses_1[i].sort(key=lambda x: x[0])
        houses_1[i][0][2] = 1
        for j in range(1, m):
            houses_1[i][j][2] = houses_1[i][j - 1][2]
            if houses_1[i][j][0] != houses_1[i][j - 1][0]:
                houses_1[i][j][2] += 1

        now_max = houses_1[i][-1][2]
        for j in range(m):
            houses_1[i][j][3] = now_max

        houses_1[i].sort(key=lambda x: x[1])

    houses_2 = []
    for i in range(m):
        houses_2.append([])
        for j in range(n):
            houses_2[i].append([streets[j][i], j, 0, 0])
        houses_2[i].sort(key=lambda x: x[0])
        houses_2[i][0][2] = 1
        for j in range(1, n):
            houses_2[i][j][2] = houses_2[i][j - 1][2]
            if houses_2[i][j][0] != houses_2[i][j - 1][0]:
                houses_2[i][j][2] += 1

        now_max = houses_2[i][-1][2]
        for j in range(n):
            houses_2[i][j][3] = now_max

        houses_2[i].sort(key=lambda x: x[1])

    results = []
    for i in range(n):
        results.append([])
        for j in range(m):
            if houses_1[i][j][2] > houses_2[j][i][2]:
                diff = houses_1[i][j][2] - houses_2[j][i][2]
                result = max(houses_1[i][j][3], houses_2[j][i][3] + diff)
            else:
                diff = houses_2[j][i][2] - houses_1[i][j][2]
                result = max(houses_2[j][i][3], houses_1[i][j][3] + diff)

            results[i].append(result)

    for r in results:
        print(''.join(str(e) + ' ' for e in r))


print(f"{f(2, 3, [[1, 2, 1], [2, 1, 2]])} = 2 2 2, 2 2 2")
print(f"{f(2, 2, [[1, 2], [3, 4]])} = 2 3, 3 2")

# n, m = list(map(int, input().split()))
# streets = []
# for i in range(n):
#     streets.append(list(map(lambda _: int(_), input().split(' '))))
# 
# f(n, m, streets)


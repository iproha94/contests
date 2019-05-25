def f(n, a_arr, m, q_arr):
    a_arr.sort()
    all_sum = sum(a_arr)
    result = []
    for q in q_arr:
        result.append(all_sum - a_arr[-q])
    return ''.join(str(e) + '\n' for e in result)


# print(f"{f(7, [7, 1, 3, 1, 4, 10, 8], 2, [3, 4])} = [27, 30]")

n = int(input())
a_arr = [*map(int, input().split())]
m = int(input())
q_arr = [*map(int, input().split())]
print(f(n, a_arr, m, q_arr))

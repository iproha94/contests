
def f(n, a_arr):
    sum_arr = []
    for i in range(n):
        for j in range(i + 1, n):
            sum_arr.append(a_arr[i] + a_arr[j])

    max_count = 0
    sum_arr.sort()

    i = 0
    j = 1
    while i < len(sum_arr):
        while j < len(sum_arr) and sum_arr[i] == sum_arr[j]:
            j += 1
        if (j - i) > max_count:
            max_count = j - i
        i = j
        j += 1

    return max_count


# print(f"{f(8, [1, 8, 3, 11, 4, 9, 2, 7])} = 3")
# print(f"{f(7, [3, 1, 7, 11, 9, 2, 12])} = 2")

n = int(input())
a_arr = list(map(lambda _: int(_), input().split(' ')))
print(f(n, a_arr))


def f(n, arr):
    i = 0
    count_start = 0
    while i < len(arr) and arr[i] == 1:
        count_start += 1
        i += 1

    if i == len(arr):
        return count_start

    max_count = count_start
    now_count = 0
    while i < len(arr):
        if arr[i] == 1:
            now_count += 1
        else:
            max_count = max(max_count, now_count)
            now_count = 0

        i += 1

    if arr[i-1] == 1:
        max_count = max(max_count, now_count + count_start)

    return max_count


# print(f"{f(5, [1, 0, 1, 0, 1])} = 2")
# print(f"{f(6, [0, 1, 0, 1, 1, 0])} = 2")
# print(f"{f(7, [1, 0, 1, 1, 1, 0, 1])} = 3")
# print(f"{f(3, [0, 0, 0])} = 0")
# 
n = int(input())
arr = list(map(int, input().split()))
print(f(n, arr))

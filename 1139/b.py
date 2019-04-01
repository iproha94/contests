
def f(n, arr):
    now_max = arr[-1]
    sum = now_max
    for i in reversed(range(len(arr) - 1)):
        if arr[i] < now_max:
            now_max = arr[i]
            sum += arr[i]
        else:
            if now_max > 0:
                now_max -= 1
            sum += now_max

    return sum


# print(f"{f(5, [1, 2, 1, 3, 6])} = 10")
# print(f"{f(5, [3, 2, 5, 4, 10])} = 20")
# print(f"{f(4, [1, 1, 1, 1])} = 1")
# 
n = int(input())
arr = list(map(int, input().split()))
print(f(n, arr))

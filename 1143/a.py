
def f(n, arr):
    last_door = arr[-1]
    i = len(arr) - 1
    while arr[i] == last_door:
        i -= 1

    return i + 1


# print(f"{f(5, [0, 0, 1, 0, 0])} = 3")
# print(f"{f(4, [1, 0, 0, 1])} = 3")
# print(f"{f(3, [1, 0, 0])} = 1")
# print(f"{f(3, [1, 1, 0])} = 2")

n = int(input())
arr = list(map(int, input().split()))
print(f(n, arr))
# 
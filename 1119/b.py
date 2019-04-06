
def f(n, h, arr):
    now = []
    rez = 0
    for i in range(n):
        now.append(arr[i])
        now.sort(reverse=True)
        now_h = 0
        for j in range(0, len(now), 2):
            try:
                second = now[j + 1]
            except Exception:
                second = 0
            now_h += max(now[j], second)
        if now_h > h:
            return rez + 1
        else:
            rez = i
    return rez + 1


# print(f"{f(5, 7, [2, 3, 5, 4, 1])} = 3")
# print(f"{f(10, 10, [9, 1, 1, 1, 1, 1, 1, 1, 1, 1])} = 4")
# print(f"{f(5, 10, [3, 1, 4, 2, 4])} = 5")

n, h = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(f(n, h, arr))

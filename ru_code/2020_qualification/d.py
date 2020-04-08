
def f(n, w_arr):
    now_weight = 0
    for i in range(len(w_arr)):
        now_weight += w_arr[i]
        # print(f"{i}: {now_weight}")
        if i > 3:
            now_weight -= w_arr[i - 4]
        if now_weight > n:
            return i - 1 if i - 1 > 0 else 0

    return len(w_arr) - 1


print(f(int(input()), [int(input()) for _ in range(int(input()))]))

# print(f"{f(120, [55, 10, 35, 12, 18, 50, 41, 10])} == 5")
# print(f"{f(30, [40, 10, 20, 10])} == 0")
# print(f"{f(40, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])} == 10")

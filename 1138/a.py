
def f(n, a_arr):
    if a_arr[0] == 1:
        now_length_1 = 1
        now_length_2 = 0
    else:
        now_length_1 = 0
        now_length_2 = 1

    max_length = 1

    for i in range(1, n):
        if a_arr[i - 1] == a_arr[i]:
            if a_arr[i] == 1:
                now_length_1 += 1
            else:
                now_length_2 += 1
        elif a_arr[i] == 1:
            now_length_1 = 1
        else:
            now_length_2 = 1

        max_length = max(max_length, min(now_length_1, now_length_2))

    return max_length * 2


# print(f"{f(7, [2, 2, 2, 1, 1, 2, 2])} = 4")
# print(f"{f(6, [1, 2, 1, 2, 1, 2])} = 2")
# print(f"{f(9, [2, 2, 1, 1, 1, 2, 2, 2, 2])} = 6")
# 
n = int(input())
a_arr = [*map(int, input().split())]
print(f(n, a_arr))

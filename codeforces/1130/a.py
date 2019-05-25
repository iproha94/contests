
def f(count, arr):
    plus = 0
    neg = 0
    zero = 0
    for a in arr:
        if a > 0:
            plus += 1
        elif a < 0:
            neg += 1
        else:
            zero += 1
    if plus >= count / 2:
        return 1
    elif neg >= count / 2:
        return -1
    else:
        return 0


# print(f"{f(5, [10, 0, -7, 2, 6])} = 4")
# print(f"{f(7, [0, 0, 1, -1, 0, 0, 2])} = 0")
# 
n = int(input())
arr = [*map(int, input().split())]
print(f(n, arr))

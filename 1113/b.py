import math


def func(n, arr):
    delta = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            sum_before = arr[i] + arr[j]
            d2 = (arr[i] + arr[j]) * (arr[i] + arr[j]) - 4 * arr[i] * arr[j]
            # print(f"d2 = {d2}")
            if d2 < 0:
                continue
            d = math.sqrt(d2)
            x1 = (arr[i] + arr[j] - d) / 2 / arr[j]
            x2 = (arr[i] + arr[j] + d) / 2 / arr[j]
            x = round(x1 + (x2 - x1) / 2)
            # print(f"ai = {arr[i]}; aj = {arr[j]}; x = {x}; x1 = {x1}; x2 = {x2}")
            if (arr[i] / x).is_integer():
                sum_after = arr[j] * x + arr[i] / x
                new_delta = sum_before - sum_after
                if new_delta > 0 and new_delta > delta:
                    delta = new_delta

    return int(sum(arr) - delta)


print(f"{func(5, [1, 2, 3, 4, 5])} = 14")
print(f"{func(4, [4, 2, 4, 4])} = 14")
print(f"{func(5, [2, 4, 2, 3, 7])} = 18")


# n = int(input())
# arr = list(map(lambda _: int(_), input().split(' ')))
# print(func(n, arr))

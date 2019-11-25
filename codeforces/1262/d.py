import os
from itertools import combinations


def f(arr, k_pos_arr):
    asc_arr = sorted(arr)
    store = {}
    for k, pos in k_pos_arr:
        if k not in store:
            new_arr = []

            ri = len(arr) - k
            while ri > 0 and asc_arr[ri] == asc_arr[ri - 1]:
                ri -= 1

            for a in arr:
                if a not in asc_arr[0: ri]:
                    new_arr.append(a)

            max_sum = 0
            max_comb = []

            for comb in combinations(new_arr, k):
                now_sum = sum(comb)
                now_comb = comb
                if now_sum > max_sum:
                    max_sum = now_sum
                    max_comb = now_comb
                elif now_sum == max_sum and max_comb > now_comb:
                    max_comb = now_comb

            store[k] = max_comb

        print(store[k][pos - 1])


if os.environ.get('DEBUG', False):
    print(
        f"{f([10, 20, 10], [[1, 1], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3]])} = 20 10 20 10 20 10")
    print(
        f"{f([1, 2, 1, 3, 1, 2, 1], [[2, 1], [2, 2], [3, 1], [3, 2], [3, 3], [1, 1], [7, 1], [7, 7], [7, 4]])} = 2 3 2 3 2 3 1 1 3")
else:
    input()
    arr = list(map(int, input().split()))
    m = int(input())
    k_pos_arr = []
    for _ in range(m):
        k_pos_arr.append(list(map(int, input().split())))
    f(arr, k_pos_arr)

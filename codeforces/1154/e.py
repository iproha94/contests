import os


def _f(n, k, num_s_map):
    results = [0] * n

    num_s_arr_sort_by_s = []
    for i in range(n):
        num_s_arr_sort_by_s.append([i, num_s_map[i]])
    num_s_arr_sort_by_s.sort(key=lambda x: -x[1])

    now_team = 2
    for num, s in num_s_arr_sort_by_s:
        if num_s_map[num]:
            now_team = 1 if now_team == 2 else 2

            results[num] = now_team
            num_s_map[num] = False

            i = num + 1
            count = 0
            while i < n and count < k:
                if num_s_map[i]:
                    results[i] = now_team
                    num_s_map[i] = False
                    count += 1
                i += 1

            i = num - 1
            count = 0
            while i >= 0 and count < k:
                if num_s_map[i]:
                    results[i] = now_team
                    num_s_map[i] = False
                    count += 1
                i -= 1

    return results


def f(n, k, arr):
    results = _f(n, k, arr)
    return ''.join(str(e) + '' for e in results)


if os.environ.get('DEBUG', False):
    print(f"{f(5, 2, [2, 4, 5, 3, 1])} = 11111")
    print(f"{f(5, 1, [2, 1, 3, 5, 4])} = 22111")
    print(f"{f(7, 1, [7, 2, 1, 3, 5, 4, 6])} = 1121122")
    print(f"{f(5, 1, [2, 4, 5, 3, 1])} = 21112")
else:
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(f(n, k, arr))

import os


def f(n, p_arr, x, a, y, b, k):
    p_arr.sort(reverse=True)

    ab_count_arr = []
    if a == 1 and b == 1:
        ab_count_arr.append([0, 0, 1])
    elif a == 1:
        ab_count_arr.append([1, 0, 0])
    elif b == 1:
        ab_count_arr.append([0, 1, 0])
    else:
        ab_count_arr.append([0, 0, 0])

    for i in range(1, n):
        ab_count_arr.append(ab_count_arr[-1].copy())

        if (i + 1) % a == 0 and (i + 1) % b == 0:
            ab_count_arr[-1][2] += 1
        elif (i + 1) % a == 0:
            ab_count_arr[-1][0] += 1
        elif (i + 1) % b == 0:
            ab_count_arr[-1][1] += 1

    for i, (a_count, b_count, ab_count) in enumerate(ab_count_arr):
        s1 = sum(p_arr[0:ab_count]) * (x + y) / 100
        s1_1 = sum(p_arr[ab_count:ab_count + a_count]) * x / 100
        s2_1 = sum(p_arr[ab_count:ab_count + b_count]) * y / 100
        s1_2 = sum(p_arr[ab_count + a_count:ab_count + a_count + b_count]) * y / 100
        s2_2 = sum(p_arr[ab_count + b_count:ab_count + b_count + a_count]) * x / 100

        if s1 + s1_1 + s1_2 >= k:
            return i + 1

        if s1 + s2_1 + s2_2 >= k:
            return i + 1

    return -1


if os.environ.get('DEBUG', False):
    print(f"{f(1, [100], 50, 1, 49, 1, 100)} = -1")
    print(f"{f(8, [100, 200, 100, 200, 100, 200, 100, 100], 10, 2, 15, 3, 107)} = 6")
    print(f"{f(3, [1000000000, 1000000000, 1000000000], 50, 1, 50, 1, 3000000000)} = 3")
    print(f"{f(5, [200, 100, 100, 100, 100], 69, 5, 31, 2, 90)} = 4")
else:
    q = int(input())
    for _ in range(q):
        n = int(input())
        p_arr = list(map(int, input().split()))
        x, a = list(map(int, input().split()))
        y, b = list(map(int, input().split()))
        k = int(input())
        print(f(n, p_arr, x, a, y, b, k))

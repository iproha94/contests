import os


def f(n, s, a_b_arr):
    i_a_b_arr = []
    for i, a_b in enumerate(a_b_arr):
        i_a_b_arr.append((i, a_b[0], a_b[1]))

    i_a_b_arr.sort(key=lambda x: (x[2], x[1]))
    # print(i_a_b_arr)

    max_count = 0
    s_arr = [True if c == '1' else False for c in s]
    for t in range(0, 1000):
        for i, a, b in i_a_b_arr:
            if t >= b and (t - b) % a == 0:
                s_arr[i] = not s_arr[i]

        # print(s_arr)
        max_count = max(len(list(filter(lambda x: x, s_arr))), max_count)

    return max_count


if os.environ.get('DEBUG', False):
    print(f"{f(3, '101', [(3, 3), (3, 2), (3, 1)])} = 2")
    print(f"{f(4, '1111', [(3, 4), (5, 2), (3, 1), (3, 2)])} = 4")
    print(f"{f(6, '011100', [(5, 3), (5, 5), (2, 4), (3, 5), (4, 2), (1, 5)])} = 6")
else:
    n = int(input())
    s = input()
    a_b_arr = []
    for i in range(n):
        a_b_arr.append(tuple(map(int, input().split())))
    print(f(n, s, a_b_arr))

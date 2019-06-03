import os


def _f(n, m, ta, tb, k, a_arr, b_arr):
    fa_arr = list(map(lambda x: x + ta, a_arr))
    fb_arr = list(map(lambda x: x + tb, b_arr))
    # print(a_arr)
    # print(fa_arr)
    # print(b_arr)
    # print(fb_arr)

    try:
        prev_i = 0
        r = 0
        for tk in range(k + 1):
            fa = fa_arr[tk]
            i = prev_i
            while b_arr[i] < fa:
                i += 1
    
            tail = k - tk
            prev_i = i
            i += tail
            r = max(r, fb_arr[i])
    except IndexError:
        return -1

    return r


def f(n, m, ta, tb, k, a_arr, b_arr):
    return _f(n, m, ta, tb, k, a_arr, b_arr)


if os.environ.get('DEBUG', False):
    print(f"{f(4, 5, 1, 1, 2, [1, 3, 5, 7], [1, 2, 3, 9, 10])} = 11")
    print(f"{f(2, 2, 4, 4, 2, [1, 10], [10, 20])} = -1")
    print(f"{f(4, 3, 2, 3, 1, [1, 999999998, 999999999, 1000000000], [3, 4, 1000000000])} = 1000000003")
    print(f"{f(4, 5, 1, 1, 4, [1, 3, 5, 7], [1, 2, 3, 9, 10])} = -1")
    print(f"{f(4, 5, 1, 1, 3, [1, 3, 5, 7], [1, 2, 3, 9, 10])} = -1")
else:
    n, m, ta, tb, k = list(map(int, input().split()))
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    print(f(n, m, ta, tb, k, a_arr, b_arr))
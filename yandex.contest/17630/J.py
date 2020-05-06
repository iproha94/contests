from math import sqrt


def f(a_arr, l_r_arr):
    s_arr = [0]
    for a in a_arr:
        s_arr.append(a * a + s_arr[-1])

    result = []
    for l, r in l_r_arr:
        result.append("%.6f" % sqrt((s_arr[r + 1] - s_arr[l]) / (r - l + 1)))

    return "".join(str(r) + '\n' for r in result)


if __name__ == "__main__":
    input()
    print(f(
        list(map(float, input().split())),
        [tuple(map(int, input().split())) for _ in range(int(input()))]
    ))

import os


def f_tl(arr):
    n1 = 0
    n2 = 0

    left_otr_counts = [0] * len(arr)
    left_otr_counts[0] = 0 if arr[0] > 0 else 1
    for i in range(1, len(arr)):
        left_otr_counts[i] = left_otr_counts[i - 1] + (0 if arr[i] > 0 else 1)

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            otr_count = left_otr_counts[j] - left_otr_counts[i] + (0 if arr[i] > 0 else 1)
            if otr_count % 2:
                n1 += 1
            else:
                n2 += 1

    return f"{n1} {n2}"

def f(arr):
    n1 = 0
    n2 = 0

    acc = 1
    otr = 0
    for a in arr:
        acc *= a
        if acc < 0:
            otr += 1

    print(otr)

    return f"{n1} {n2}"


if os.environ.get('DEBUG', False):
    print(f"{f([5, -3, 3])} = 4 2")
    print(f"{f([5, -3, 3, -1, 1])} = 8 7")
    print(f"{f([5, -3, 3, -1, -1])} = 9 6")
    print(f"{f([4, 2, -4, 3, 1, 2, -4, 3, 2, 3])} = 28 27")
    print(f"{f([-1, -2, -3, -4, -5])} = 9 6")
else:
    n = int(input())
    arr = list(map(int, input().split()))
    print(f(arr))

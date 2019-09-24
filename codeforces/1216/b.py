import os


def f(arr):
    i_a_arr = [(i + 1, a) for i, a in enumerate(arr)]
    i_a_arr.sort(key=lambda x: -x[1])

    result = 0
    for i in range(len(i_a_arr)):
        result += i_a_arr[i][1] * i + 1

    return f"{result}\n{''.join(str(i) + ' ' for i, a in i_a_arr)}"


if os.environ.get('DEBUG', False):
    print(f"{f([20, 10, 20])} = 43 [1 3 2]")
    print(f"{f([10, 10, 10, 10])} = 64 [2 1 4 3]")
    print(f"{f([5, 4, 5, 4, 4, 5])} = 69 [6 1 3 5 2 4]")
    print(f"{f([1, 4])} = 3 [2 1]")
else:
    input()
    arr = list(map(int, input().split()))
    print(f(arr))

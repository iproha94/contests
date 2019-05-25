
def _f(n, arr):
    arr.sort()

    arr_1 = []
    arr_2 = []

    arr_1.append(arr[0])

    if len(arr) > 1:
        arr_2.append(arr[1])

    for i in range(2, len(arr)):
        if arr[i] == arr_1[-1] and arr[i] == arr_2[-1]:
            return False, [], []
        elif arr[i] == arr_1[-1]:
            arr_2.append(arr[i])
        else:
            arr_1.append(arr[i])

    arr_2.sort(reverse=True)

    return True, arr_1, arr_2


def f(n, arr):
    result, arr_1, arr_2 = _f(n, arr)
    if result:
        print("YES")
        print(len(arr_1))
        print(''.join(str(e) + ' ' for e in arr_1))
        print(len(arr_2))
        print(''.join(str(e) + ' ' for e in arr_2))
    else:
        print("NO")


# print(f"{f(7, [7, 2, 7, 3, 3, 1, 4])} = YES | 2 | 3 7 | 5 | 7 4 3 2 1")
# print(f"{f(5, [4, 3, 1, 5, 3])} = YES | 1 | 3 | 4 | 5 4 3 1")
# print(f"{f(5, [1, 1, 2, 1, 2])} = NO")
# print(f"{f(5, [0, 1, 2, 3, 4])} = YES | 0 |  | 5 | 4 3 2 1 0")
# print(f"{f(1, [10])} = YES | 1 | 10 | 0 |  |")
# f"{f(3, [10, 10, 10])} = NO"
# 
n = int(input())
arr = list(map(int, input().split()))
f(n, arr)

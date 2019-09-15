import os


def f(arr):
    arr.sort()
    result = []
    result.append(arr[0])
    for i in range(1, len(arr)):
        flag = False
        for j in range(len(result)):
            if arr[i] % result[j] == 0:
                flag = True
                break

        if not flag:
            result.append(arr[i])

    return len(result)


if os.environ.get('DEBUG', False):
    print(f"{f([10, 2, 3, 5, 4, 2])} = 3")
    print(f"{f([100, 100, 100, 100])} = 1")
    print(f"{f([7, 6, 5, 4, 3, 2, 2, 3])} = 4")
else:
    int(input())
    print(f(list(map(int, input().split()))))

import os


def f(arr):
    result = [1] * len(arr)
    min2 = 10
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            j = i - 1
            while j >= 0 and arr[j] > arr[i]:
                if j != i - 1 and arr[j] > arr[j + 1]:
                    return '-'

                min2 = min(min2, arr[j])
                result[j] = 2
                j -= 1
        elif arr[i] > min2:
            result[i] = 2
            min2 = arr[i] 

    return ''.join(str(e) for e in result)


if os.environ.get('DEBUG', False):
    print(f"{f([0,4,0,4,2,5,5,2,4,6,4,4])} = 121212211211")
    print(f"{f([0])} = 1")
    print(f"{f([1,2,3,4,5,6,7,8,9])} = 222222222")
    print(f"{f([9,8])} = 21")
    print(f"{f([9,8,7])} = -")
    print(f"{f([0,4,0,2,3,5,5,2,4,6,4,4])} = 121122211211")
    print(f"{f([4,1,5])} = 212")
else:
    t = int(input())
    for _ in range(t):
        int(input())
        print(f(list(map(int, input()))))

def f(arr):
    arr.sort()
    result = []
    if len(arr) % 2:
        for a in arr[0::2]:
            result.append(a)
        for a in arr[-2::-2]:
            result.append(a)
    else:
        for a in arr[0::2]:
            result.append(a)
        for a in arr[-1::-2]:
            result.append(a)

    return ''.join(str(e) + ' ' for e in result)


# print(f"{f([2, 1, 1, 3, 2])} = [1 2 3 2 1]")
# print(f"{f([30, 10, 20])} = [10 20 30]")
# print(f"{f([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])} = [10, 12, 14, 16, 18, 19, 17, 15, 13, 11]")
# 
n = int(input())
arr = [*map(int, input().split())]
print(f(arr))

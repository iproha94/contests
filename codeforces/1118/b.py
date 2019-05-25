def func(n, arr):
    result = 0
    a0 = 0
    b0 = sum(arr[2::2])
    c0 = 0
    d0 = sum(arr[1::2])

    # print(f"{a0} {b0} {c0} {d0} ")
    if a0 + d0 == b0 + c0:
        result += 1

    for i in range(1, len(arr)):
        f = arr[i]
        e = arr[i - 1]
        a = a0 + (0 if i % 2 else e)
        b = d0 - f
        c = c0 + (e if i % 2 else 0)
        d = b0

        a0 = a
        b0 = b
        c0 = c
        d0 = d

        # print(f"{a0} {b0} {c0} {d0} ")
        if a0 + d0 == b0 + c0:
            result += 1

    return result


print(f"{func(4, [1, 4, 3, 3])} = 2")
print(f"{func(7, [5, 5, 4, 5, 5, 5, 6])} = 2")
print(f"{func(8, [4, 8, 8, 7, 8, 4, 4, 5])} = 2")
print(f"{func(9, [2, 3, 4, 2, 2, 3, 2, 2, 4])} = 3")


# n = int(input())
# arr = [*map(int, input().split())]
# print(func(n, arr))

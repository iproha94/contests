
def _f(n, arr, result, base, it):
    if it == n:
        return result

    r = -1
    for i in range(n):
        if base[i]:
            continue

        if it == 0 or i + 1 - result[-1] == arr[it - 1]:
            result.append(i + 1)
            base[i] = 1
            r = _f(n, arr, result, base, it + 1)

            if r == -1:
                base[i] = 0
                result.pop()
            else:
                break

    return r


def f(n, arr):
    base = [0] * n
    result = _f(n, arr, [], base, 0)
    if result != -1:
        return ''.join(str(e) + ' ' for e in result)
    else:
        return -1


print(f"{f(3, [-2, 1])} = 3 1 2")
print(f"{f(5, [1, 1, 1, 1])} = 1 2 3 4 5")
print(f"{f(4, [-1, 2, 2])} = -1")

# 
# n = int(input())
# arr = list(map(int, input().split()))
# print(f(n, arr))
# 
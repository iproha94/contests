
def _f(n, arr):
    number_count_map = {}
    for a in arr:
        if number_count_map.get(a, None) is None:
            number_count_map[a] = 1
        else:
            number_count_map[a] += 1

    max_number = list(number_count_map.keys())[0]
    for dict_key in list(number_count_map.keys()):
        if number_count_map[dict_key] > number_count_map[max_number]:
            max_number = dict_key

    empties = []
    if arr[0] != max_number:
        empties.append([0, 0])

    for i in range(1, len(arr)):
        if arr[i] == max_number and arr[i - 1] != max_number:
            empties[-1][1] = i - 1
        elif arr[i] != max_number and arr[i - 1] != max_number:
            empties[-1][1] = i
        elif arr[i] != max_number and arr[i - 1] == max_number:
            empties.append([i, i])

    result = []
    for e in empties:
        if e[1] != len(arr) - 1:
            for i in reversed(range(e[0], e[1] + 1)):
                if arr[i] > max_number:
                    result.append((2, i + 1, i + 2))
                elif arr[i] < max_number:
                    result.append((1, i + 1, i + 2))
        else:
            for i in range(e[0], e[1] + 1):
                if arr[i] > max_number:
                    result.append((2, i + 1, i))
                elif arr[i] < max_number:
                    result.append((1, i + 1, i))

    return result


def f(n, arr):
    result = _f(n, arr)
    print(len(result))
    for r in result:
        print(''.join(str(e) + ' ' for e in r))


# f(5, [2, 4, 6, 6, 6])
# print(f"2 | 1 2 3 | 1 1 2 |")
# f(3, [2, 8, 10])
# print(f"2 | 2 2 1 | 2 3 2|")
# f(4, [1, 1, 1, 1])
# print(f"0")

n = int(input())
arr = list(map(int, input().split()))
f(n, arr)

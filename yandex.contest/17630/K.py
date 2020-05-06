
def f(arr):
    d = {}
    prev = None
    m = []
    for a in arr:
        if a == prev:
            m.append(m[-1])
        else:
            d.setdefault(a, 0)
            d[a] += 1
            m.append(d[a])

        prev = a

    a_counts = {}
    for a in arr:
        a_counts[a] = a_counts.get(a, 0) + 1

    result = []
    deleted = set()
    for i in range(len(arr)):
        if m[i] != 1:
            result.append(arr[i])
        elif d[arr[i]] == 1 and a_counts[arr[i]] > 1 and arr[i] not in deleted:
            result.append(arr[i])
            deleted.add(arr[i])

    return f"{len(result)}\n" + "".join(str(r) + ' ' for r in result)


if __name__ == "__main__":
    input()
    arr = list(map(int, input().split()))
    print(f(arr))

def f(arr):
    r1 = 0
    r2 = 1
    while r2 != len(arr) and arr[r2] == arr[r1]:
        r2 += 1
    if r2 == len(arr):
        return "NO"

    r = []
    r.append((r1, r2))
    for i in range(len(arr)):
        if i in [r1, r2]:
            continue
        if arr[i] != arr[r1]:
            r.append((r1, i))
        else:
            r.append((r2, i))

    s = "YES"
    for i, j in r:
        s += f"\n{i + 1} {j + 1}"
    return s


if __name__ == "__main__":
    for _ in range(int(input())):
        int(input())
        print(f(list(map(int, input().split()))))


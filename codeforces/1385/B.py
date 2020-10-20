
def f(arr):
    result = []
    for a in arr:
        if a not in result:
            result.append(a)
    return "".join(str(e) + ' ' for e in result)


if __name__ == "__main__":
    for _ in range(int(input())):
        int(input())
        print(f(list(map(int, input().split()))))

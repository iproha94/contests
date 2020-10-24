
def f(arr):
    l = 0
    while arr[l] == 0:
        l += 1
    r = len(arr) - 1
    while arr[r] == 0:
        r -= 1
    c = 0
    for i in range(l, r):
        if arr[i] == 0:
            c += 1
    return c


if __name__ == "__main__":
    for _ in range(int(input())):
        int(input())
        print(f(list(map(int, input().split()))))


def f(arr):
    if len(arr) <= 2:
        return 0

    i = -1
    while i > -len(arr) and arr[i] == arr[i - 1]:
        i -= 1
    if i == -len(arr):
        return 0

    while i > -len(arr) and arr[i] <= arr[i - 1]:
        i -= 1
    if i == -len(arr):
        return 0

    while i > -len(arr) and arr[i] >= arr[i - 1]:
        i -= 1
    if i == -len(arr):
        return 0

    return len(arr) + i


if __name__ == "__main__":
    for _ in range(int(input())):
        int(input())
        print(f(list(map(int, input().split()))))

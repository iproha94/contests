
def f(arr):
    max_a = max(arr)
    for i in range(len(arr)):
        if arr[i] != max_a:
            continue
        if i == 0 and max_a != arr[i + 1]:
            return i + 1
        elif i == len(arr) - 1 and max_a != arr[i - 1]:
            return i + 1
        elif i != 0 and i != len(arr) - 1 and (max_a != arr[i + 1] or max_a != arr[i - 1]):
            return i + 1

    return -1


if __name__ == "__main__":
    for _ in range(int(input())):
        int(input())
        print(f(list(map(int, input().split()))))


import os


def f(arr):
    if len(arr) == 1:
        return True

    i = 1
    while i < len(arr) and arr[i] == arr[i - 1]:
        i += 1

    if i == len(arr):
        return True

    if arr[i] < arr[i - 1]:
        while i < len(arr) and arr[i] <= arr[i - 1]:
            i += 1
    else:
        while i < len(arr) and arr[i] >= arr[i - 1]:
            i += 1

    if i == len(arr):
        return False

    return True


if os.getenv('TEST_MODE', False):
    print("------TEST MODE------")
    print(f"{f([3, 1, 5, 3])} = True\n")
    print(f"{f([3, 2, 1])} = False\n")
    print(f"{f([7331])} = True\n")
    print(f"{f([3, 1, 5, 6])} = True\n")
    print("---------------------")
elif __name__ == "__main__":
    for _ in range(int(input())):
        input()
        arr = list(map(int, input().split()))
        print('YES' if f(arr) else 'NO')

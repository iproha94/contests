import os


def f(n, k):
    if n == 1 and k == 1:
        print("Yes")
        print("1")
        return
    if k == 1:
        print("No")
        return
    if n ** 2 / k != int(n ** 2 / k):
        print("No")
        return

    print("Yes")
    for i in range(n):
        print(" ".join(str((j + i) % k + 1) for j in range(n)))


if os.getenv('TEST_MODE', False):
    print("------TEST MODE------")
    # print(f"{f(8, 2)} = Yes\n")
    # print(f"{f(2, 1)} = No\n")
    # print(f"{f(3, 3)} = Yes\n")
    # print(f"{f(1, 3)} = No\n")
    # print(f"{f(5, 3)} = No\n")
    print(f"{f(10, 8)} = \n")
    print("---------------------")
elif __name__ == "__main__":
    f(*tuple(map(int, input().split())))

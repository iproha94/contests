import os


def f(x, y):
    if y % x:
        return 0, 0
    return 1, y // x


if os.getenv('TEST_MODE', False):
    print("------TEST MODE------")
    print(f"{f(3, 75)} = 2 5")
    print(f"{f(100, 100)} = 3 1")
    print(f"{f(42, 13)} = 0 0")
    print(f"{f(3, 33)} = 1 11")
    print(f"{f(1, 1)} = 1 1")
    print(f"{f(10, 1)} = 0 0")
    print(f"{f(1, 10)} = 1 10")
    print(f"{f(3, 18)} = 1 6")
    print(f"{f(12, 312)} = 1 26")
    print("---------------------")
elif __name__ == "__main__":
    for _ in range(int(input())):
        x, y = tuple(map(int, input().split()))
        a1, b1 = f(x, y)
        print(f"{a1} {b1}")

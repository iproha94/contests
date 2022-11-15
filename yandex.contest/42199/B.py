import os


def f(n, b, flag = 0):
    if b == 1:
        return n

    ln = 0
    nn = n
    while n:
        a = n % 10
        n //= 10
        ln += 1
    # print(f"a = {a}, ln = {ln}")

    if ln == 1:
        return a // b + flag
    if a % b:
        return ((a // b) + 1) * ((9 // b) + 1) ** (ln - 1) - 1
    return (a // b) * ((9 // b) + 1) ** (ln - 1) - 1 + f(nn - a * (10 ** (ln - 1)), b, 1)


if os.getenv('TEST_MODE', False):
    print("------TEST MODE------")
    print(f"{f(7, 3)} = 2\n")
    print(f"{f(6, 3)} = 2\n")
    print(f"{f(36, 3)} = 6\n")
    print(f"{f(7508, 3)} = 191\n")
    print(f"{f(10, 1)} = 10\n")
    print(f"{f(11, 2)} = 4\n")
    print(f"{f(1000000000000000000, 7)} = 262143\n")
    print("---------------------")
elif __name__ == "__main__":
    for _ in range(int(input())):
        print(f(*tuple(map(int, input().split()))))

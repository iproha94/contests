import os


def f(s):
    n1, n2 = ord(s[0]) - 96, ord(s[1]) - 96
    # print(n1, n2)
    return (n1 - 1) * 26 + n2 - n1 + (1 if n1 > n2 else 0)


if os.getenv('TEST_MODE', False):
    print("------TEST MODE------")
    print(f"{f('ab')} = 1\n")
    print(f"{f('ac')} = 2\n")
    print(f"{f('az')} = 25\n")
    print(f"{f('ba')} = 26\n")
    print(f"{f('bc')} = 27\n")
    print(f"{f('zx')} = 649\n")
    print(f"{f('zy')} = 650\n")
    print("---------------------")
elif __name__ == "__main__":
    for _ in range(int(input())):
        print(f(input()))

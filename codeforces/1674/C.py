import os


def f(s, t):
    if len(t) == 1 and t[0] == 'a':
        return 1
    if 'a' in t:
        return -1
    return 2 ** len(s)


if os.getenv('TEST_MODE', False):
    print("------TEST MODE------")
    print(f"{f('aaaa', 'a')} = 1\n")
    print(f"{f('aa', 'abc')} = -1\n")
    print(f"{f('a', 'b')} = 2\n")
    print(f"{f('aaaa', 'bc')} = \n")
    print("---------------------")
elif __name__ == "__main__":
    for _ in range(int(input())):
        print(f(input(), input()))

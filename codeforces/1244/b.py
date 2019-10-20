import os


def f(s):
    for i in range(len(s) // 2 + 1):
        if s[i] == '1':
            return (len(s) - i) * 2
        elif s[len(s) - i - 1] == '1':
            return (len(s) - i) * 2

    return len(s)


if os.environ.get('DEBUG', False):
    print(f"{f('00100')} = 6")
    print(f"{f('00000000')} = 8")
    print(f"{f('11111')} = 10")
    print(f"{f('110')} = 6")
    print(f"{f('1')} = 2")
    print(f"{f('0')} = 1")
    print(f"{f('0001')} = 8")
    print(f"{f('0010')} = 6")
else:
    t = int(input())
    for _ in range(t):
        input()
        print(f(input()))

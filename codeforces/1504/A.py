import os


def f(s):
    for i in range(len(s)):
        if s[i] != 'a':
            return f'YES\n{s}a'
        if s[-i-1] != 'a':
            return f'YES\na{s}'
    return "NO"


if os.getenv('TEST_MODE', False):
    print("------TEST MODE------")
    print(f"{f('cbabc')} = Y")
    print(f"{f('ab')} = Y")
    print(f"{f('zza')} = Y")
    print(f"{f('ba')} = Y")
    print(f"{f('a')} = N")
    print(f"{f('nutforajaroftuna')} = Y")
    print(f"{f('abab')} = Y")
    print(f"{f('bbabba')} = Y")
    print("---------------------")
elif __name__ == "__main__":
    for _ in range(int(input())):
        print(f(input()))

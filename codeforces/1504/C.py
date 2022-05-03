import os


def f(s):
    i = 0
    j = 0
    s1 = ""
    s2 = ""
    for k, c in enumerate(s):
        if c == '1':
            if i > 0 and j > 0:
                if k < len(s) - 1 and s[k + 1] == '0' and i == 1 and j == 1:
                    i += 1
                    j += 1
                    s1 += '('
                    s2 += '('
                else:
                    i -= 1
                    j -= 1
                    s1 += ')'
                    s2 += ')'
            else:
                i += 1
                j += 1
                s1 += '('
                s2 += '('
        else:
            if i == 0 and j > 0:
                i += 1
                j -= 1
                s1 += '('
                s2 += ')'
            elif i > 0 and j == 0:
                i -= 1
                j += 1
                s1 += ')'
                s2 += '('
            elif i == 0 and j == 0:
                return 'NO'
            else:
                if j > i:
                    i += 1
                    j -= 1
                    s1 += '('
                    s2 += ')'
                else:
                    i -= 1
                    j += 1
                    s1 += ')'
                    s2 += '('

    return "NO" if i != 0 or j != 0 else f'YES\n{s1}\n{s2}'


if os.getenv('TEST_MODE', False):
    print("------TEST MODE------")
    print(f"{f('101101')} = Y")
    print(f"{f('1001101101')} = Y")
    print(f"{f('1100')} = N")
    print(f"{f('110101')} = Y (())() ((()))")
    print("---------------------")
elif __name__ == "__main__":
    for _ in range(int(input())):
        input()
        print(f(input()))

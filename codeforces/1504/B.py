import os


def f(s, r):
    sc0 = 0
    sc1 = 0
    rc0 = 0
    rc1 = 0
    eq_exist = False
    neq_exist = False
    l = 0
    for i in range(len(s)):
        sc0 += s[i] == '0'
        sc1 += s[i] == '1'
        rc0 += r[i] == '0'
        rc1 += r[i] == '1'

        if s[i] == r[i]:
            eq_exist = True
        if s[i] != r[i]:
            neq_exist = True

        if (sc0 == sc1 and rc0 != rc1) or (sc0 != sc1 and rc0 == rc1):
            return 'NO'
        elif sc0 == sc1:
            if eq_exist and neq_exist:
                return 'NO'

            sc0 = 0
            sc1 = 0
            rc0 = 0
            rc1 = 0
            eq_exist = False
            neq_exist = False
            l = i + 1
        else:
            pass

    return 'YES' if s[l:] == r[l:] else 'NO'


if os.getenv('TEST_MODE', False):
    print("------TEST MODE------")
    print(f"{f('0111010000', '0100101100')} = Y")
    print(f"{f('0000', '0000')} = Y")
    print(f"{f('1111', '0000')} = Y")
    print(f"{f('001', '000')} = N")
    print(f"{f('010101010101', '100110011010')} = Y")
    print(f"{f('000111', '110100')} = N")
    print(f"{f('0', '0')} = Y")
    print(f"{f('0', '1')} = N")
    print(f"{f('000', '111')} = N")
    print("---------------------")
elif __name__ == "__main__":
    for _ in range(int(input())):
        input()
        print(f(input(), input()))

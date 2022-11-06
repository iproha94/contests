import os
import string


def c_to_d(c):
    return int(c) if c in string.digits else ord(c) - 65 + 10


def f1(s: str):
    result = []
    plus = True
    try:
        op1, op2 = s.split(' + ')
    except Exception:
        try:
            op1, op2 = s.split(' - ')
            plus = False
        except Exception:
            for c in s:
                result.append(c_to_d(c))
            return result

    op2 = op2.zfill(len(op1))
    op1 = op1.zfill(len(op2))
    # print(f"f1: op1={op1}")
    # print(f"f1: op2={op2}")

    result1 = []
    for c in op1:
        result1.append(c_to_d(c))

    result2 = []
    for c in op2:
        result2.append(c_to_d(c))

    # print(f"f1: result1={result1}")
    # print(f"f1: result2={result2}")

    if plus:
        for i in range(len(result1)):
            result.append(result1[i] + result2[i])
    else:
        for i in range(len(result1)):
            result.append(result1[i] - result2[i])

    return result


def f(s):
    min_sys = s[0]
    for c in s:
        if c in ' +-=':
            continue
        if c > min_sys:
            min_sys = c
    min_sys = c_to_d(min_sys)

    op1, op2 = s.split(' = ')
    r1 = f1(op1)
    r2 = f1(op2)
    r1.reverse()
    r2.reverse()

    for i in range(len(r1), len(r2)):
        r1.append(0)
    for i in range(len(r2), len(r1)):
        r2.append(0)
    # print(r1)
    # print(r2)

    for i in range(len(r2)):
        r1[i] -= r2[i]

    max_sys = min_sys + 1
    for r in r1:
        if abs(r) > max_sys:
            max_sys = abs(r)
    # print(r1)

    max_sys *= 10
    for ss in range(min_sys + 1, max_sys + 1):
        s = 0
        for i in range(len(r1)):
            s += r1[i] * (ss ** i)

        if s == 0:
            return ss

    return -1


if os.getenv('TEST_MODE', False):
    print("------TEST MODE------")
    print(f"{f('2 + 2 = 11 - 1')} = 4\n")
    print(f"{f('1 = 1')} = 2\n")
    print(f"{f('2 = 3')} = -1\n")
    print(f"{f('B = A + 1')} = 12\n")
    print("---------------------")
elif __name__ == "__main__":
    print(f(input()))

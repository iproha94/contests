import os


def f(s):
    # o_count = s.count('o')
    n_count = s.count('n')
    # e_count = s.count('e')

    z_count = s.count('z')
    # r_count = s.count('r')

    result = ""

    for _ in range(n_count):
        result += '1 '

    for _ in range(z_count):
        result += '0 '

    return result


if os.environ.get('DEBUG', False):
    print(f"{f('ezor')} = 0")
    print(f"{f('nznooeeoer')} = 1 1 0")
else:
    input()
    print(f(input()))

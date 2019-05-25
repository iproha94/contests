import os
from math import fabs

alphabet_A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_C = 'CDEFGHIJKLMNOPQRSTUVWXYZAB'
alphabet_T = 'TUVWXYZABCDEFGHIJKLMNOPQRS'
alphabet_G = 'GHIJKLMNOPQRSTUVWXYZABCDEF'

target = 'ACTG'

A_count_map = {}
C_count_map = {}
T_count_map = {}
G_count_map = {}

for i in range(26):
    A_count_map[alphabet_A[i]] = int(min(fabs(i), fabs(26 - i)))
    C_count_map[alphabet_C[i]] = int(min(fabs(i), fabs(26 - i)))
    T_count_map[alphabet_T[i]] = int(min(fabs(i), fabs(26 - i)))
    G_count_map[alphabet_G[i]] = int(min(fabs(i), fabs(26 - i)))


def _f(n, s):
    result = 10000000000
    for i in range(len(s) - 3):
        result = min(
            result,
            A_count_map[s[i]] + C_count_map[s[i + 1]] + T_count_map[s[i + 2]] + G_count_map[s[i + 3]]
        )

    return result


def f(n, s):
    return _f(n, s)


if os.environ.get('DEBUG', False):
    print(f"{f(4, 'ZCTH')} = 2")
    print(f"{f(5, 'ZDATG')} = 5")
    print(f"{f(6, 'AFBAKC')} = 16")
else:
    n = int(input())
    s = input()
    print(f(n, s))

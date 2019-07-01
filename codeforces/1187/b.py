import os

b_c_map = {}


def _f(n, s, t):
    if not b_c_map:
        for i, c in enumerate(s):
            if b_c_map.get(c, None) is None:
                b_c_map[c] = [i]
            else:
                b_c_map[c].append(i)

    t_c_map = {}
    for c in t:
        if t_c_map.get(c, None) is None:
            t_c_map[c] = 1
        else:
            t_c_map[c] += 1

    m = 0
    for key, value in t_c_map.items():
        m = max(m, b_c_map[key][value - 1])

    return m + 1


def f(n, s, t):
    return _f(n, s, t)


if os.environ.get('DEBUG', False):
    print(f"{f(9, 'arrayhead', 'arya')} = 5")
    print(f"{f(9, 'arrayhead', 'harry')} = 6")
    print(f"{f(9, 'arrayhead', 'ray')} = 5")
    print(f"{f(9, 'arrayhead', 'r')} = 2")
    print(f"{f(9, 'arrayhead', 'areahydra')} = 9")
else:
    n = int(input())
    s = input()
    for _ in range(int(input())):
        print(f(n, s, input()))

import os


def _f(s, t, p):
    try:
        i = 0
        for c in s:
            i = t.index(c, i)
            i += 1
    except Exception:
        return 'NO'

    s_dict = {}
    for c in s:
        if s_dict.get(c, None) is None:
            s_dict[c] = 1
        else:
            s_dict[c] += 1

    for c in p:
        if s_dict.get(c, None) is None:
            s_dict[c] = 1
        else:
            s_dict[c] += 1

    try:
        for c in t:
            if s_dict[c] == 0:
                raise Exception()
            else:
                s_dict[c] -= 1
    except Exception:
        return 'NO'

    return 'YES'


def f(s, t, p):
    return _f(s, t, p)


if os.environ.get('DEBUG', False):
    print(f"{f('ab', 'acxb', 'cax')} = Y")
    print(f"{f('a', 'aaaa', 'aaabbcc')} = Y")
    print(f"{f('a', 'aaaa', 'aabbcc')} = N")
    print(f"{f('ab', 'baaa', 'aaaaa')} = N")
else:
    q = int(input())
    for i in range(q):
        print(f(input(), input(), input()))

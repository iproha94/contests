import os


def f(s, t):
    s_set = set()
    for c in s:
        s_set.add(c)

    t_set = set()
    for c in t:
        t_set.add(c)

    for s in s_set:
        for t in t_set:
            if s == t:
                return 'YES'

    return 'NO'


if os.environ.get('DEBUG', False):
    print(f"{f('xabb', 'aabx')} = YES")
    print(f"{f('technocup', 'technocup')} = YES")
    print(f"{f('a','z')} = NO")
else:
    q = int(input())
    for _ in range(q):
        print(f(input(), input()))

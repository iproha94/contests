import os


def _f(s):
    count = 0
    for c in s:
        if c == 'a':
            count += 1
    n = len(s)
    
    return min(count * 2 - 1, n)


def f(s):
    return _f(s)


if os.environ.get('DEBUG', False):
    print(f"{f('xaxxxxa')} = 3")
    print(f"{f('aaabaa')} = 6")
else:
    print(f(input()))

import os


def f(s):
    new_s:str = s[0]
    count = 0
    prev_char = new_s[-1]
    for i in range(1, len(s)):
        if i % 2:
            if s[i] == prev_char:
                count += 1
                new_s += 'a' if s[i] == 'b' else 'b'
            else:
                new_s += s[i]
        else:
            new_s += s[i]

        prev_char = new_s[-1]

    return f"{count}\n{new_s}"


if os.environ.get('DEBUG', False):
    print(f"{f('bbbb')} = 2 abba")
    print(f"{f('ababab')} = 0 ababab")
    print(f"{f('aa')} = 1 ba")
else:
    int(input())
    print(f(input()))

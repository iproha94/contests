import os


def f(s):
    result = [''] * len(s)
    min_char = s[0]
    result[0] = 'Mike'
    for i in range(1, len(s)):
        if min_char < s[i]:
            result[i] = 'Ann'
        else:
            result[i] = 'Mike'
            min_char = s[i]

    return ''.join(e + '\n' for e in result)


if os.environ.get('DEBUG', False):
    print(f"{f('abba')} = M A A M")
    print(f"{f('cba')} = M M M")
else:
    print(f(input()))

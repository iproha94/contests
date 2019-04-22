import os


def _f(s):
    new_s = ""
    last_a_index = -1
    last_a_index_in_new_s = -1
    for i, c in enumerate(s):
        if c == 'a':
            last_a_index = i
            last_a_index_in_new_s = len(new_s)
        else:
            new_s += c

    if new_s == "":
        return s

    if last_a_index == -1:
        if s[len(s) // 2:] == s[:len(s) // 2]:
            return s[:len(s) // 2]
        else:
            return ':('

    last_a_index_in_new_s_save = last_a_index_in_new_s
    while last_a_index_in_new_s < len(new_s):
        if new_s[:last_a_index_in_new_s] == new_s[last_a_index_in_new_s:]:
            return s[:last_a_index + (last_a_index_in_new_s - last_a_index_in_new_s_save + 1)]
        last_a_index_in_new_s += 1
    return ':('


def f(s):
    return _f(s)


if os.environ.get('DEBUG', False):
    print(f"{f('aaaaa')} = aaaaa")
    print(f"{f('aacaababc')} = :(")
    print(f"{f('ababacacbbcc')} = ababacac")
    print(f"{f('baba')} = :(")
    print(f"{f('bbb')} = :(")
    print(f"{f('bbbb')} = bb")
    print(f"{f('acc')} = ac")
    print(f"{f('caa')} = :(")
    print(f"{f('b')} = :(")
    print(f"{f('bb')} = b")
    print(f"{f('a')} = a")
    print(f"{f('bbbc')} = :(")
else:
    print(f(input()))

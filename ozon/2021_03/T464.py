
def f(s):
    r = ""
    i = 0
    while s[i].isalpha():
        r += s[i]
        i += 1

    s_count = ''
    while s[i].isdigit():
        s_count += s[i]
        i += 1

    flag = 1
    j = i
    while flag:
        j += 1
        if s[j] == ']':
            flag -= 1
        elif s[j] == '[':
            flag += 1

    r += s[i + 1:j] * int(s_count)
    r += s[j+1:]
    return r if r.isalpha() else f(r)


# print(f("3[a]2[bc]"))  # aaabcbc
# print(f("3[a2[c]]"))  # accaccacc
# print(f("2[abc]3[cd]ef"))  # abcabccdcdcdef
# print(f("abc3[cd]xyz"))  # abccdcdcdxyz

if __name__ == "__main__":
    print(f(input()))

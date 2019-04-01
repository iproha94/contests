
def f(n, c_str, a_str):
    only_a = []
    only_c = []
    nothing = []
    all = []
    for i in range(n):
        if c_str[i] == '1' and a_str[i] == '0':
            only_c.append(i + 1)
        elif a_str[i] == '1' and c_str[i] == '0':
            only_a.append(i + 1)
        elif c_str[i] == '1' and a_str[i] == '1':
            all.append(i + 1)
        else:
            nothing.append(i + 1)

    group_1 = []
    group_2 = []

    while len(all) > 0 and len(only_a) > 0:
        group_1.append(all.pop())
        group_2.append(only_a.pop())

    while len(all) > 0 and len(only_c) > 0:
        group_1.append(only_c.pop())
        group_2.append(all.pop())

    while len(only_a) > 0 and len(only_c) > 0:
        group_1.append(only_c.pop())
        group_2.append(only_a.pop())

    while len(only_a) > 0 and len(nothing) > 0:
        group_1.append(only_a.pop())
        group_2.append(nothing.pop())

    while len(only_c) > 0 and len(nothing) > 0:
        group_1.append(nothing.pop())
        group_2.append(only_c.pop())

    while len(all) > 0 and len(all) % 2 == 0:
        group_1.append(all.pop())
        group_2.append(all.pop())

    if len(only_c) > 0 or len(only_a) > 0 or len(all) > 0:
        return -1
    elif len(nothing) % 2 == 1:
        return -1
    else:
        return ''.join(str(e) + ' ' for e in group_1 + nothing[::2])


# print(f"{f(4, '0011', '0101')} = 1 4")
# print(f"{f(6, '000000', '111111')} = -1")
# print(f"{f(4, '0011', '1100')} = 4 3")
# print(f"{f(8, '00100101', '01111100')} = 1 2 3 6")
# print(f"{f(4, '1111', '1111')} = 1 3")
# 
n = int(input())
c_str = input()
a_str = input()
print(f(n, c_str, a_str))

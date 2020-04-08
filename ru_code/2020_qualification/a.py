
def f(s):
    spaces = 0
    for i, c in enumerate(s[1:]):
        if c == ' ':
            spaces += 1
        elif spaces in [0, 1]:
            return 'unsafe'
        else:
            spaces = 0
    return 'safe'


print(f(input()))
#
# print(f"{f('s  o  c  i  a  l  d   i  s  t  a  n  c   i  n  g')} = safe")
# print(f"{f('virus')} = unsafe")
#
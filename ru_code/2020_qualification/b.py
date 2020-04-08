
def f(n):
    s = 0
    for i in range(1, n + 1):
        if i == 1:
            s += 1
        elif i == 2:
            s += 1
        else:
            s = s * 2
    return s

print(f(int(input())))
#
# print(f"{f(1)} = 1")
# print(f"{f(2)} = 2")
# print(f"{f(3)} = 4")
# print(f"{f(4)} = 8")
# print(f"{f(5)} = 16")
#
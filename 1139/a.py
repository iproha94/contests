
def f(n, s):
    counts = [0] * n
    if int(s[n - 1]) % 2 == 0:
        counts[n - 1] = 1
    for i in reversed(range(n - 1)):
        counts[i] = counts[i + 1]
        if int(s[i]) % 2 == 0:
            counts[i] += 1

    return sum(counts)


# print(f"{f(4, '1357')} = 0")
# print(f"{f(1, '1')} = 0")
# print(f"{f(1, '2')} = 1")
# print(f"{f(4, '1234')} = 6")
# print(f"{f(4, '2244')} = 10")
# print(f"{f(4, '2468')} = 10")
# 
n = int(input())
s = input()
print(f(n, s))
# 

def f(n, arr):
    for a in arr:
        l = list(map(ord, a))
        l.sort()
        result = 'Yes'
        for i in range(1, len(l)):
            if l[i] - l[i - 1] != 1:
                result = 'No'
                break
        print(result)


f(8, ["fced", "xyz", "r", "dabcef", "az", "aa", "bad", "babc"])
print("Yes Yes Yes Yes No No No No")

# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(input())
# f(n, arr)
# 
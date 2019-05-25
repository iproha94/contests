
def f(n, k):
    if k > n / 2:
        k = n - k + 1
    return (n + 1) + n + (k - 2) + n


# print(f"{f(2, 2)} = 6")
# print(f"{f(4, 2)} = 13")
# print(f"{f(5, 1)} = 15")

n, k = list(map(int, input().split()))
print(f(n, k))

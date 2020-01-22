def f(a, b, c, n):
    if a >= b and a >= c:
        diff = n - (a - b + a - c)
    elif b >= a and b >= c:
        diff = n - (b - a + b - c)
    elif c >= a and c >= b:
        diff = n - (c - a + c - b)
    else:
        raise ValueError

    return 'YES' if diff >= 0 and diff % 3 == 0 else 'NO'


t = int(input())
for _ in range(t):
    print(f(*list(map(int, input().split()))))

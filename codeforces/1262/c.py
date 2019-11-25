import os


def f(k, s):
    arr = []
    r = 0
    for i, c in enumerate(s):
        r += (1 if c == '(' else -1)
        if r == 0:
            arr.append(i)
        elif r < 0:
            break

    print(arr)

    return 0


if os.environ.get('DEBUG', False):
    print(f"{f(2, '()(())()')} = 4: 3 4, 1 1, 5 8, 2 2")
    print(f"{f(3, '))()()()((')} = 3: 4 10, 1 4, 6 7")
    print(f"{f(1, '()')} = 0")
    print(f"{f(1, ')(')} = 1: 1 2")
else:
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        s = input()
        print(f(k, s))

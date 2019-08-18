import os


def f(n):
    if n % 2 == 0:
        return "NO"

    arr = [2*n]
    for _ in range(n):
        if _ % 2 == 0:
            arr.append(arr[-1] - n)
        else:
            arr.append(arr[-1] + n)

        if _ != n - 1:
            arr.append(arr[-1] - 1)

    result = [0] * (2 * n)
    for i, e in enumerate(arr):
        result[e - 1] = i + 1

    # for i in range(2 * n):
    #     s = 0
    #     for j in range(n):
    #         s += result[(i + j) % (2 * n)]
    #     print(s)
    return f"YES\n{''.join(str(e) + ' ' for e in result)}"


if os.environ.get('DEBUG', False):
    print(f"{f(3)} = YES: 1 4 5 2 3 6")
    print(f"{f(4)} = NO")
    print(f"{f(5)} = ...")
    print(f"{f(7)} = ...")
else:
    n = int(input())
    print(f(n))

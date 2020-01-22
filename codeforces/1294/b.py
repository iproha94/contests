import os


def f(x_y_arr):
    x_y_arr.sort(key=lambda x: (x[0], x[1]))

    x_prev = 0
    y_prev = 0
    result = ""
    for x, y in x_y_arr:
        if x < x_prev or y < y_prev:
            return 'NO'
        elif x == x_prev:
            result += 'U' * (y - y_prev)
        elif y == y_prev:
            result += 'R' * (x - x_prev)
        else:
            result += 'R' * (x - x_prev)
            result += 'U' * (y - y_prev)

        x_prev = x
        y_prev = y

    return f"YES\n{result}"


if os.environ.get('DEBUG', False):
    print(f"{f([(1, 3), (1, 2), (3, 3), (5, 5), (4, 3)])} = RUUURRRRUU")
    print(f"{f([(1, 0), (0, 1)])} = NO")
    print(f"{f([(4, 3)])} = RRRRUUU")
else:
    for _ in range(int(input())):
        x_y_arr = []
        for _ in range(int(input())):
            x_y_arr.append(tuple(map(int, input().split())))
        print(f(x_y_arr))

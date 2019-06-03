import os


def f_debug(temps, ttdd):
    n = len(temps) // 2

    temps1 = []
    temps1.append((temps[n], temps[n], temps[n]))
    for i in range(n + 1, len(temps)):
        temps1.append((temps[i], min(temps[i], temps1[-1][1]), max(temps[i], temps1[-1][2])))

    temps2 = []
    for i in range(n, -1, -1):
        temps2.append(temps[i])


    temps2 = []
    temps2.append((temps[n], temps[n], temps[n]))
    for i in range(n - 1, -1, -1):
        temps2.append((temps[i], min(temps[i], temps2[-1][1]), max(temps[i], temps2[-1][2])))

    min_t = min(temps2[-ttdd[2]][1], temps1[ttdd[3]][1])
    max_t = max(temps2[-ttdd[2]][2], temps1[ttdd[3]][2])

    if ttdd[0] <= min_t:
        if ttdd[1] >= min_t:
            return "yes"
        else:
            return "no"
    elif ttdd[0] <= max_t:
        return "yes"
    else:
        return "no"


def f_prod(temps1, temps2, ttdd):
    min_t = min(temps2[-ttdd[2]][1], temps1[ttdd[3]][1])
    max_t = max(temps2[-ttdd[2]][2], temps1[ttdd[3]][2])

    if ttdd[0] <= min_t:
        if ttdd[1] >= min_t:
            return "yes"
        else:
            return "no"
    elif ttdd[0] <= max_t:
        return "yes"
    else:
        return "no"


if os.environ.get('DEBUG', False):
    print(f"{f_debug([2, 4, 5, -2, 2], [-1, -1, -1, 1])} = yes")
    print(f"{f_debug([2, 4, 5, -2, 2], [0, 10, -1, 0])} = yes")
    print(f"{f_debug([2, 4, 5, -2, 2], [6, 8, -2, 2])} = no")
    print(f"{f_debug([2, 4, 5, -2, 2], [3, 3, -1, 0])} = no")
else:
    _ = int(input())
    temps = list(map(int, input().split()))

    n = len(temps) // 2

    temps1 = []
    temps1.append((temps[n], temps[n], temps[n]))
    for i in range(n + 1, len(temps)):
        temps1.append((temps[i], min(temps[i], temps1[-1][1]),
                       max(temps[i], temps1[-1][2])))

    temps2 = []
    for i in range(n, -1, -1):
        temps2.append(temps[i])

    temps2 = []
    temps2.append((temps[n], temps[n], temps[n]))
    for i in range(n - 1, -1, -1):
        temps2.append((temps[i], min(temps[i], temps2[-1][1]),
                       max(temps[i], temps2[-1][2])))

    q = int(input())
    for i in range(q):
        ttdd = list(map(int, input().split()))
        print(f_prod(temps1, temps2, ttdd))
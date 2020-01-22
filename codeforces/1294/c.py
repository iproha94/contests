import os
import math


def f(n):
    result = []
    now = 2
    while len(result) < 2 and now < math.sqrt(n):
        if n % now == 0:
            result.append(now)
            n //= now
        now += 1

    if len(result) == 2 and n not in result:
        return f"YES\n{result[0]} {result[1]} {n}"
    else:
        return "NO"


if os.environ.get('DEBUG', False):
    print(f"{f(64)} = 2 4 8 ")
    print(f"{f(32)} = NO")
    print(f"{f(97)} = NO")
    print(f"{f(2)} = NO")
    print(f"{f(12345)} = 3 5 823")
else:
    for _ in range(int(input())):
        print(f(int(input())))

import itertools, math


def f1(a, b):
    result = [a + b, a - b, b - a, a * b]
    if a:
        result.append(b / a)
    if b:
        result.append(a / b)
    return result


def f(hand):
    diff = 21
    for perm in list(itertools.permutations(hand)):
        for i in f1(perm[0], perm[1]):
            for j in f1(i, perm[2]):
                for k in f1(j, perm[3]):
                    now_diff = 21 - int(k)
                    if k == int(k) and (
                        math.fabs(diff) > math.fabs(now_diff) or (
                            diff < 0 and math.fabs(diff) == math.fabs(now_diff)
                        )
                    ):
                        diff = now_diff

    return 21 - diff


# print(f"{f([2, 4, 3, 1])} = 21")
# print(f"{f([4, 4, 4, 3])} = 20")
#
print(f(list(map(int, input().split()))))

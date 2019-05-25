

def f(cnt1, cnt2, cnt3, cnt4):
    if cnt1 == cnt4:
        if cnt3 == 0:
            return 1
        elif cnt1 > 0:
            return 1

    return 0


# print(f"{f(*(3, 1, 4, 3))} = 1")
# print(f"{f(*(0, 0, 0, 0))} = 1")
# print(f"{f(*(1, 2, 3, 4))} = 0")


print(f(int(input()), int(input()), int(input()), int(input())))

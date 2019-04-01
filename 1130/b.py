from math import fabs


def f(n, arr):
    nowA = 0
    nowB = 0

    all_lenA = 0
    all_lenB = 0

    for i in range(0, n):
        finding_house = i + 1

        next1 = None
        next2 = None

        nextA_left = nowA
        nextA_right = nowA

        nextB_left = nowB
        nextB_right = nowB

        while next1 is None:
            if nextA_left >= 0:
                if arr[nextA_left] == finding_house:
                    next1 = nextA_left
                    nextA_left -= 1
                    break

                nextA_left -= 1

            if nextB_left >= 0:
                if arr[nextB_left] == finding_house:
                    next1 = nextB_left
                    nextB_left -= 1
                    break

                nextB_left -= 1

            if nextA_right < len(arr):
                if arr[nextA_right] == finding_house:
                    next1 = nextA_right
                    nextA_right += 1
                    break

                nextA_right += 1

            if nextB_right < len(arr):
                if arr[nextB_right] == finding_house:
                    next1 = nextB_right
                    nextB_right += 1
                    break

                nextB_right += 1

        while next2 is None:
            if nextA_left >= 0:
                if arr[nextA_left] == finding_house:
                    next2 = nextA_left
                    break

                nextA_left -= 1

            if nextB_left >= 0:
                if arr[nextB_left] == finding_house:
                    next2 = nextB_left
                    break

                nextB_left -= 1

            if nextA_right < len(arr):
                if arr[nextA_right] == finding_house:
                    next2 = nextA_right
                    break

                nextA_right += 1

            if nextB_right < len(arr):
                if arr[nextB_right] == finding_house:
                    next2 = nextB_right
                    break

                nextB_right += 1

        lenA_1 = int(fabs(next1 - nowA))
        lenB_1 = int(fabs(next1 - nowB))

        lenA_2 = int(fabs(next2 - nowA))
        lenB_2 = int(fabs(next2 - nowB))

        if lenA_1 + lenB_2 < lenB_1 + lenA_2:
            all_lenA += lenA_1
            all_lenB += lenB_2
            nowA = next1
            nowB = next2
        else:
            all_lenA += lenA_2
            all_lenB += lenB_1
            nowA = next2
            nowB = next1

    return all_lenA + all_lenB


print(f"{f(3, [1, 1, 2, 2, 3, 3])} = 9")
print(f"{f(2, [2, 1, 1, 2])} = 5")
print(f"{f(4, [4, 1, 3, 2, 2, 3, 1, 4])} = 17")
# 
# n = int(input())
# arr = list(map(int, input().split()))
# print(f(n, arr))

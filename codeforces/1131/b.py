
def f(scores):
    count = 1
    x0 = 0
    y0 = 0
    for x, y in scores:
        if x == 0 and y == 0:
            continue

        mn = min(x, y)
        mx0 = max(x0, y0)
        if mn >= mx0:
            count += mn - mx0 + (1 if x0 != y0 else 0)

        x0 = x
        y0 = y

    return count


# print(f"{f([(2, 0), (3, 1), (3, 4)])} = 2")
# print(f"{f([(0, 0), (0, 0), (0, 0)])} = 1")
# print(f"{f([(5, 4)])} = 5")
# print(f"{f([(0, 1), (2, 2),])} = 3")
# print(f"{f([(0, 1), (3, 2),])} = 3")
# print(f"{f([(0, 2), (4, 3),])} = 3")
# print(f"{f([(0, 2), (4, 2),])} = 2")
# print(f"{f([(0, 2), (1, 3), (4, 3),])} = 2")
# print(f"{f([(0, 2), (1, 3)])} = 1")
# print(f"{f([(0, 0), (3, 3)])} = 4")
# 

scores = []
n = int(input())
for i in range(n):
    scores.append(map(lambda _: int(_), input().split(' ')))
print(f(scores))


# 
# def f(scores):
#     count = 0
#     x0 = scores[0][0]
#     y0 = scores[0][1]
#     x_i = scores[1][0]
#     y = scores[1][1]
# 
#     mn = min(x_i, y)
#     mx0 = max(x0, y0)
#     if mn >= mx0:
#         count += mn - mx0 + (1 if x0 != y0 else 0)
# 
#     return count
# 
# print("\n2:1")
# print(f"{f([(2, 1), (4, 3)])} = 2")
# print(f"{f([(2, 1), (3, 3)])} = 2")
# print(f"{f([(2, 1), (3, 4)])} = 2")
# print(f"{f([(2, 1), (2, 1)])} = 0")
# 
# print("\n2:2")
# print(f"{f([(2, 2), (4, 3)])} = 1")
# print(f"{f([(2, 2), (3, 3)])} = 1")
# print(f"{f([(2, 2), (3, 4)])} = 1")
# print(f"{f([(2, 2), (2, 2)])} = 0")
# print(f"{f([(2, 2), (4, 4)])} = 2")
# 
# print("\n1:2")
# print(f"{f([(1, 2), (4, 3)])} = 2")
# print(f"{f([(1, 2), (3, 3)])} = 2")
# print(f"{f([(1, 2), (3, 4)])} = 2")
# print(f"{f([(1, 2), (1, 2)])} = 0")
# 
# 
# print("\n1:5")
# print(f"{f([(1, 5), (3, 8)])} = 0")
# print(f"{f([(1, 5), (3, 7)])} = 0")
# print(f"{f([(1, 5), (4, 7)])} = 0")
# print(f"{f([(1, 5), (6, 5)])} = 1")
# print(f"{f([(1, 5), (6, 6)])} = 2")
# print(f"{f([(1, 5), (6, 7)])} = 2")

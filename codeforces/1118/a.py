

def func(n, a, b):
    sum1 = n * a
    sum2 = (n // 2) * b + (n %  2) * a
    return min(sum1, sum2)

# input_data = [
#     (10, 1, 3),
#     (7, 3, 2),
#     (1, 1000, 1),
#     (1000000000000, 42, 88),
# ]


input_data = []
q = int(input())
for i in range(q):
    input_data.append(map(lambda _: int(_), input().split(' ')))

for data in input_data:
    print(func(*data))

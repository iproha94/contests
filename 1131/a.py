

def f(w1, h1, w2, h2):
    return (w1 + h1 + h2) * 2 + 4


# print(f"{f(*(2, 1, 2, 1))} = 12")
# print(f"{f(*(2, 2, 1, 2))} = 16")
# print(f"{f(*(7, 2, 2, 2))} = 26")


input_data = map(lambda _: int(_), input().split(' '))
print(f(*input_data))

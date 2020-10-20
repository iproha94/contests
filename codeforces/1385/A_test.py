from A import f

print(f"{f(3, 2, 3)} = YES 3 2 1")
print(f"{f(100, 100, 100)} = YES 100 100 100")
print(f"{f(50, 49, 49)} = NO")
print(f"{f(10, 30, 20)} = NO")
print(f"{f(1, 1000000000, 1000000000)} = YES 1 1 1000000000")

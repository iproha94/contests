from D import f

print(f"{f([1, 2, 2, 1, 3])} = YES 1 3, 3 5, 5 4, 1 2")
print(f"{f([1, 1, 1])} = NO")
print(f"{f([1, 1000, 101, 1000])} = YES 1 2, 2 3, 3 4")
print(f"{f([1, 2, 3, 4])} = YES 1 2, 1 3, 1 4")

print(f"{f([1, 2, 2, 2])} = YES 1 2, 1 3, 1 4")
print(f"{f([2, 2, 2, 1])} = YES")

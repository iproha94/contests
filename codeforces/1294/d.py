def f(x, mex, mod_count):
    while mod_count.get(mex % x, False):
        mod_count[mex % x] -= 1
        mex += 1

    return mex


q, x = list(map(int, input().split()))
mod_count = {}
mex = 0
result = ""
for _ in range(q):
    if x != 1:
        mod = int(input()) % x
        mod_count[mod] = mod_count.get(mod, 0) + 1
        mex = f(x, mex, mod_count)
    else:
        mex = _ + 1

    result += str(mex)
    result += '\n'

print(result)

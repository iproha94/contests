import os


plan = [0, 1, 2, 0, 2, 1, 0, 0, 1, 2, 0, 2, 1, 0]


def _sub_f(start, now, a, b, c, sum):
    if now == 7:
        return sum
    elif plan[start + now] == 0 and a == 0:
        return sum
    elif plan[start + now] == 1 and b == 0:
        return sum
    elif plan[start + now] == 2 and c == 0:
        return sum
    elif plan[start + now] == 0:
        return _sub_f(start, now + 1, a - 1, b, c, sum + 1)
    elif plan[start + now] == 1:
        return _sub_f(start, now + 1, a, b - 1, c, sum + 1)
    elif plan[start + now] == 2:
        return _sub_f(start, now + 1, a, b, c - 1, sum + 1)


def _f(a, b, c):
    a_whole_weeks = a // 3
    b_whole_weeks = b // 2
    c_whole_weeks = c // 2

    whole_weeks = min(a_whole_weeks, b_whole_weeks, c_whole_weeks)

    a_residue = a - whole_weeks * 3
    b_residue = b - whole_weeks * 2
    c_residue = c - whole_weeks * 2

    d0 = _sub_f(0, 0, a_residue, b_residue, c_residue, 0)
    d1 = _sub_f(1, 0, a_residue, b_residue, c_residue, 0)
    d2 = _sub_f(2, 0, a_residue, b_residue, c_residue, 0)
    d3 = _sub_f(3, 0, a_residue, b_residue, c_residue, 0)
    d4 = _sub_f(4, 0, a_residue, b_residue, c_residue, 0)
    d5 = _sub_f(5, 0, a_residue, b_residue, c_residue, 0)
    d6 = _sub_f(6, 0, a_residue, b_residue, c_residue, 0)
    return whole_weeks * 7 + max(d0, d1, d2, d3, d4, d5, d6)


def f(a, b, c):
    return _f(a, b, c)


if os.environ.get('DEBUG', False):
    print(f"{f(2, 1, 1)} = 4")
    print(f"{f(3, 2, 2)} = 7")
    print(f"{f(1, 100, 1)} = 3")
    print(f"{f(30, 20, 10)} = 39")
else:
    a, b, c = list(map(int, input().split()))
    print(f(a, b, c))

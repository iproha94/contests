import os


def f(q_arr):
    p_arr = []
    prev_q = None
    for q in q_arr:
        if q != prev_q:
            p_arr.append(q)
            prev_q = q
        else:
            p_arr.append(None)

    last_p_set = set()
    for p in p_arr:
        if p:
            last_p_set.add(p)

    all_p_set = set()
    for i in range(1, len(q_arr) + 1):
        all_p_set.add(i)

    unused_p_set = all_p_set - last_p_set
    for i in range(len(p_arr)):
        if p_arr[i]:
            continue

        p = unused_p_set.pop()
        if q_arr[i] >= p:
            p_arr[i] = p
        else:
            return -1

    return "".join(str(e) + ' ' for e in p_arr)


if os.environ.get('DEBUG', False):
    print(f"{f([1, 4, 4, 4])} = 1, 4, 2, 3")
    print(f"{f([1, 3, 4, 5, 5])} = 1 3 4 5 2")
    print(f"{f([1, 1, 3, 4])} = -1")
    print(f"{f([2, 2])} = 2 1")
    print(f"{f([1])} = 1")
else:
    t = int(input())
    for _ in range(t):
        int(input())
        print(f(list(map(int, input().split()))))

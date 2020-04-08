import math

abs = math.fabs


def rook_attack(wk, wr, bk):
    if wr[1] < bk[1]:
        if wr[0] == bk[0] and (
                wk[0] != wr[0] or wk[1] < wr[1] or wk[1] > bk[1]):
            return True
        if wr[1] == bk[1] and (
                wk[1] != wr[1] or wk[0] < wr[0] or wk[0] > bk[0]):
            return True
    elif wr[1] > bk[1]:
        if wr[0] == bk[0] and (
                wk[0] != wr[0] or wk[1] < bk[1] or wk[1] > wr[1]):
            return True
        if wr[1] == bk[1] and (
                wk[1] != wr[1] or wk[0] < bk[0] or wk[0] > wr[0]):
            return True
    elif bk[0] > wr[0] and (wk[1] != bk[1] or wk[1] > bk[1] or wk[1] < wr[1]):
        return True
    elif bk[0] < wr[0] and (wk[1] != bk[1] or wk[1] > wr[1] or wk[1] < bk[1]):
        return True
    else:
        return False


def king_attack(wk, bk):
    return abs(wk[0] - bk[0]) <= 1 and abs(wk[1] - bk[1]) <= 1


def f(wk, wr, bk):
    if king_attack(wk, bk):
        return 'Strange'

    has_step = False
    for new_bk in [
        (bk[0] - 1, bk[1] - 1),
        (bk[0] - 1, bk[1]),
        (bk[0] - 1, bk[1] + 1),
        (bk[0], bk[1] - 1),
        (bk[0], bk[1] + 1),
        (bk[0] + 1, bk[1] - 1),
        (bk[0] + 1, bk[1]),
        (bk[0] + 1, bk[1] + 1),
    ]:
        if new_bk[0] < 1 or new_bk[1] < 1 or new_bk[0] > 8 or new_bk[1] > 8:
            continue

        if new_bk == wr or not (king_attack(wk, new_bk) or rook_attack(wk, wr, new_bk)):
            has_step = True
            break

    is_attack = rook_attack(wk, wr, bk)
    if has_step and not is_attack:
        return 'Normal'
    elif has_step and is_attack:
        return 'Check'
    elif not has_step and not is_attack:
        return 'Stalemate'
    elif not has_step and is_attack:
        return 'Checkmate'


task = input().split()
print(f(
    (ord(task[0][0]) - 96, int(task[0][1])),
    (ord(task[1][0]) - 96, int(task[1][1])),
    (ord(task[2][0]) - 96, int(task[2][1])),
))

# print(f"{f((2, 2), (1, 3), (3, 4))} == Normal")
# print(f"{f((1, 1), (2, 2), (5, 2))} == Check")

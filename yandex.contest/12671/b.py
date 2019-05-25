import os


def _f(k, pairs):
    players = {}
    for pair in pairs:
        if players.get(pair[0], None) is None:
            players[pair[0]] = 1
        else:
            players[pair[0]] += 1
        if players.get(pair[1], None) is None:
            players[pair[1]] = 1
        else:
            players[pair[1]] += 1

    for i in range(1, k):
        lose_players = {k: v for k, v in players.items() if v == i}
        win_players = {k: v for k, v in players.items() if v != i}
        if len(lose_players) != 2 ** (k - i):
            return None
        else:
            players = win_players

    return players


def f(k, pairs):
    result = _f(k, pairs)
    if result is not None and len(list(result.keys())) == 2:
        return f'{list(result.keys())[0]} {list(result.keys())[1]}'
    else:
        return 'NO SOLUTION'


if os.environ.get('DEBUG', False):
    print(f"{f(3, [('g', 'a'), ('s', 'ka'), ('s', 'g'), ('b', 'i'), ('p', 'b'), ('g', 'i'), ('i', 'k'), ])} = i g")
    print(f"{f(2, [('i', 'p'), ('p', 'b'), ('b', 'i')])} = no")
else:
    k = int(input())
    pairs = []
    for i in range(2 ** k - 1):
        pairs.append(input().split())
    print(f(k, pairs))

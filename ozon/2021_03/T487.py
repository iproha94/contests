# тип умею рекурсию писать!
# поиск в глубину, поэтому не найдет самой короткой цепочки, но такого и нет в
# условии задачи;


def f(m, finish, next, chain):
    for i in m.get(next, []):
        if i in chain:
            continue

        next_chain = chain.copy()
        next_chain.append(i)

        if i == finish:
            return next_chain

        r = f(m, finish, i, next_chain)
        if r:
            return r

    return []


def search_acquaintances_chain(m, start, finish):
    return f(m, finish, start, [start])


# (1, 11) -> [1, 3, 8, 11]
# (1, 15) -> []
# (3, 4) -> [3, 8, 1, 2, 4]
m1 = {
    1: [2, 3],
    2: [4, 5, 6],
    3: [7, 8, 2, 4],
    8: [10, 11, 1],
}

# (1, 15) -> [1, 3, 15]
m2 = {
    1: [2, 3],
    2: [1],
    3: [1, 15],
}

m3 = {}

# print(search_acquaintances_chain(m3, 1, 15))

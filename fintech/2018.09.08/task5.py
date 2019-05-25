"""
Задача 5
Представитель Tinkoff.ru должен отвезти карточки по N пунктам.
Он смотрит для каждой пары пунктов A и B, существуют ли общественный
транспорт без пересадок, чтобы добраться из A в B
(причем существование пути из A в B не гарантирует,
что существует путь из B в A). Существует ли такой набор пунктов,
по которым можно кататься по кругу?

Входные данные
Первая строка содержит N(1⩽N⩽100).
Следующие N строк содержат по N чисел каждая: 0 или 1.
j-ое число в i-ой строке равно 1 тогда и только тогда,
когда существует транспорт без пересадок, идущий из пункта i в пункт j.
Из пункта i в пункт i транспорта без пересадок нет ни для какого i.

Результат работы
Выведите 1, если существует такой набор пунктов, по которым можно кататься
по кругу, и 0 в ином случае.

Примеры
Входные данные
2
0 1
1 0
Результат работы
1
"""


def cyclic(g):
    """ from https://codereview.stackexchange.com/questions/86021/check-if-a-directed-graph-contains-a-cycle
    Return True if the directed graph g has a cycle.
    g must be represented as a dictionary mapping vertices to
    iterables of neighbouring vertices. For example:

    >>> cyclic({1: (2,), 2: (3,), 3: (1,)})
    True
    >>> cyclic({1: (2,), 2: (3,), 3: (4,)})
    False

    """
    path = set()

    def visit(vertex):
        path.add(vertex)
        for neighbour in g.get(vertex, ()):
            if neighbour in path or visit(neighbour):
                return True
        path.remove(vertex)
        return False

    return any(visit(v) for v in g)


count = int(input())
points = []
for i in range(count):
    raw = input().split(' ')
    points.append(list(map(lambda _: int(_), raw)))

d = {}
for i in range(count):
    near = []
    for j in range(count):
        if points[i][j]:
            near.append(j)

    d[i] = near

# d = {0: [], 1: [3,], 2: [], 3: [4,], 4: [2, ]}
r = cyclic(d)
print(1 if r else 0)

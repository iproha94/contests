"""
Задача 4
Таня отметила на доске NN точек, а Арина хочет найти все различные
равнобедренные треугольники, которые можно построить на этих точках.
Найдите число таких треугольников. Два треугольника считаются различными,
если множества их вершин различны.

Входные данные
Первая строка содержит N(3⩽n⩽1500). Следующие N строк содержит 2 целых
числа X_i, Y_i – координаты уникальных точек (∣Xi∣,∣Xi∣⩽1000).

Результат работы
Выведите ответ на задачу.

Примеры
Входные данные
4
0 3
3 0
0 -3
-3 0
Результат работы
4
"""


import math


def f(a, b, c):
    len1 = math.sqrt(abs(b[0] - a[0]) * abs(b[0] - a[0]) + abs(b[1] - a[1]) * abs(b[1] - a[1]))
    if not len1:
        return False

    len2 = math.sqrt(abs(c[0] - a[0]) * abs(c[0] - a[0]) + abs(c[1] - a[1]) * abs(c[1] - a[1]))
    if not len2:
        return False

    len3 = math.sqrt(abs(b[0] - c[0]) * abs(b[0] - c[0]) + abs(b[1] - c[1]) * abs(b[1] - c[1]))
    if not len3:
        return False

    if len1 == len2 or len1 == len3 or len3 == len2:
        return True

    return False


count = int(input())
points = []
for i in range(count):
    raw = input().split(' ')
    x, y = map(lambda _: int(_), raw)
    points.append([x, y])

# points = [[0, 3], [3, 0], [0, -3], [-3, 0]]

result_count = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        for k in range(j + 1, len(points)):
            if f(points[i], points[j], points[k]):
                result_count += 1

print(result_count)

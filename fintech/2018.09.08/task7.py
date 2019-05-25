"""
Задача 7
Эмилия нарисовала несколько точек, а Лера выбирает из них тройку и рисует
треугольник. Какой максимальный периметр треугольника может получиться у
выбранного треугольника?

Входные данные
Первая строка содержит N (1⩽N⩽1000)
Следующие N строк содержи два числа, координаты точки
(по модулю не превосходящие 10^5).

Результат работы
Выведите максимальный периметр с точностью до 15 знаков.

Примеры
Входные данные
4
0 0
0 4
2 0
3 0
Результат работы
12

"""

import math


def f(a, b, c):
    len1 = math.sqrt(abs(b[0] - a[0]) * abs(b[0] - a[0]) + abs(b[1] - a[1]) * abs(b[1] - a[1]))
    if not len1:
        return 0

    len2 = math.sqrt(abs(c[0] - a[0]) * abs(c[0] - a[0]) + abs(c[1] - a[1]) * abs(c[1] - a[1]))
    if not len2:
        return 0

    len3 = math.sqrt(abs(b[0] - c[0]) * abs(b[0] - c[0]) + abs(b[1] - c[1]) * abs(b[1] - c[1]))
    if not len3:
        return 0

    return len1 + len2 + len3


count = int(input())
points = []
for i in range(count):
    raw = input().split(' ')
    x, y = map(lambda _: int(_), raw)
    points.append([x, y])

# count = 4
# points = [[0, 0], [0, 4], [2, 0], [3, 0]]

my_max = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        for k in range(j + 1, len(points)):
            my_max = max(my_max, f(points[i], points[j], points[k]))

rounded_value = round(my_max, 15)
if rounded_value == int(rounded_value):
    print(int(rounded_value))
else:
    print(rounded_value)


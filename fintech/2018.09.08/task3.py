"""
Задача 3
Марина выписывает числа от 1 до N в ряд таким образом, чтобы в полученном
массиве было строго K инверсий. Напишите программу, которая найдет такой ряд.

Входные данные
Первая строка содержит N и K.
Результат работы
Выведите ряд разделенный пробелом, если такая расстановка существует и -1,
если это невозможно.

Примеры
Входные данные
4 0
Результат работы
1 2 3 4
"""


def recover_straight(ls):
    n = len(ls)
    result = [0 for _ in range(n)]
    curr = 1
    for k in ls:
        j = 0
        for i in range(n):
            if result[i] == 0:
                if j == k:
                    result[i] = curr
                    break
                else:
                    j += 1
        curr += 1
    return result


input = input().split(' ')
n, k = map(lambda _: int(_), input)

# n = 4
# k = 0

ti = [0 for i in range(n)]

for i in reversed(range(n)):
    for j in range(i):
        if k > 0:
            ti[j] += 1
            k -= 1

if k > 0:
    print(-1)
else:
    r = recover_straight(ti)
    str_r = ''
    for i in r:
        str_r += str(i)
        str_r += ' '

    print(str_r.strip())


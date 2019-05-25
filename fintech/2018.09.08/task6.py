"""
Задача 6
Правильный торт "Графские развалины" состоит из нескольких слоев безе,
где в каждом слое меньше безе, чем в слое под ним.
У Кати было N безе, сколько различных правильных тортов "Графские развалины"
она могла приготовить, если она использовала все безе?

Входные данные
Первая строка содержит число N(1⩽N⩽1000).
Результат работы
Выведите число правильных тортов.

Примеры
Входные данные
11
Результат работы
12
"""


def f(arr, count, res=0):
    if arr[0] == count:
        return res + 1

    lsum = sum(arr)
    if lsum < count:
        new_arr = arr[:]
        new_arr.append(new_arr[-1] + 1)
        return f(new_arr, count, res)
    elif lsum > count:
        new_arr = arr[:-1]
        new_arr[-1] += 1
        return f(new_arr, count, res)
    else:
        new_arr = arr[:-1]
        new_arr[-1] += 1
        return f(new_arr, count, res + 1)


count = int(input())
print(f([1], count))

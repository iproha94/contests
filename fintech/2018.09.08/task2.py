"""
Задача 2
Во время контеста на летние стажировки у разработчиков закончилось
свободное место на сервере и они решили оперативно сжать хранимые на
сайте тексты. Они справились с задачей и воспользовались простейшим алгоритмом:
подряд идущие одинаковые буквы (если их строго больше одной) заменили на
число повторений + букву. Например, слово "HELLO" сжимается в "HE2LO".
Пока они занимались сжатием строк, системные администраторы выделили
дополнительной памяти и теперь стоит обратная задача: нужно написать
программу, которая вернет строки в исходный вид.

Входные данные
Первая строка содержит строку, состоящую из заглавных латинских букв и цифр,
длина строки не превышает 10^3

Результат работы
Выведите строку в несжатом виде.

Примеры
Входные данные
HE2LO
Результат работы
HELLO
"""

# compressed_raw = 'HE2LO'
compressed_raw = input()

source_raw = ''

i = 0
while i < len(compressed_raw):
    c = compressed_raw[i]
    if c.isalpha():
        source_raw += c
        i += 1
        continue

    repit = ''
    while c.isdigit():
        repit += c
        i += 1
        c = compressed_raw[i]

    for j in range(int(repit)):
        source_raw += c

    i += 1

print(source_raw)

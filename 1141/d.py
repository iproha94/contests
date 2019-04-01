
def f(n, str1, str2):
    list1 = []
    for i in range(len(str1)):
        list1.append([str1[i], i + 1, False])

    list2 = []
    for i in range(len(str2)):
        list2.append([str2[i], i + 1, False])

    list1.sort(key=lambda x: x[0])
    list2.sort(key=lambda x: x[0])

    i = 0
    while i < len(list1) and list1[i][0] == '?':
        i += 1

    j = 0
    while j < len(list2) and list2[j][0] == '?':
        j += 1

    result = []
    while i < len(list1) and j < len(list2):
        if list1[i][0] == list2[j][0]:
            list1[i][2] = True
            list2[j][2] = True
            result.append((list1[i][1], list2[j][1]))
            i += 1
            j += 1
        elif list1[i][0] < list2[j][0]:
            i += 1
        else:
            j += 1

    list1 = list(filter(lambda x: not x[2], list1))
    list2 = list(filter(lambda x: not x[2], list2))
    list2.sort(key=lambda x: x[0], reverse=True)

    i = 0
    while i < len(list1) and i < len(list2):
        if list1[i][0] == '?' or list2[i][0] == '?':
            result.append((list1[i][1], list2[i][1]))
        i += 1

    print(len(result))
    for l_r in result:
        print(f"{l_r[0]} {l_r[1]}")


# print(f"{f(10, 'codeforces', 'dodivthree')} = 5, 7 8, 4 9, 2 2, 9 10, 3 1")
# print(f"{f(7, 'abaca?b', 'zabbbcc')} = 5, 6 5, 2 3, 4 6, 7 4, 1 2")
# print(f"{f(9, 'bambarbia', 'hellocode')} = 0")
# print(f"{f(10, 'code??????', '??????test')} = 10, 6 2, 1 6, 7 3, 3 5, 4 8, 9 7, 5 1, 2 4, 10 9, 8 10")

n = int(input())
str1 = input()
str2 = input()
f(n, str1, str2)

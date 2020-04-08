
def f(k, stroy, offset=0):
    l = 0
    r = len(stroy)
    go_to_rec = False
    while l != r:
        if stroy[l:l+k+1].count('w') == 1:
            print(''.join(str(i + 1 + offset) + ' ' for i in range(l,l+k+1)))
            l = l+k+1
        elif stroy[r-k-1:r].count('w') == 1:
            print(''.join(str(i + 1 + offset) + ' ' for i in range(r-k-1,r)))
            r = r-k-1
        else:
            new_l = l + k
            new_r = r - 1
            success = True
            while stroy[l:new_l].count('w') + stroy[new_r:r].count('w') != 1:
                new_l -= 1
                new_r -= 1
                if new_l == l:
                    success = False
                    break

            if success:
                print(''.join(str(i + 1 + offset) + ' ' for i in list(range(l, new_l)) + list(range(new_r, r))))
                l = new_l
                r = new_r
            else:
                go_to_rec = True
                break

    if go_to_rec:
        new_l = l + (r - l) - k // 2
        new_r = new_l + k + 1

        new_l_2 = new_l
        new_r_2 = new_r
        while stroy[new_l:new_r].count('w') != 1 or stroy[new_l_2:new_r_2].count('w') != 1:
            new_l += 1
            new_r += 1
            new_l_2 -= 1
            new_r_2 -= 1
        if stroy[new_l:new_r].count('w') == 1:
            print(''.join(str(i + 1 + offset) + ' ' for i in range(new_l, new_r)))
            f(k, stroy[0:new_l], 0)
            f(k, stroy[new_r:], new_r)
        else:
            print(''.join(str(i + 1 + offset) + ' ' for i in range(new_l_2, new_r_2)))
            f(k, stroy[0:new_l_2], 0)
            f(k, stroy[new_r_2:], new_r_2)

# f(2, 'wwvwvvvvvvwv')
# print(f" = 10 11 12 | 1 8 9 | 2 6 7 | 3 4 5")
# f(2, 'vwvvwv')
# print(f" = 1 2 3 | 4 5 6")

f(list(map(int, input().split()))[1], input())


def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(int(n))
   return primfac


def f(n, m):
    arr_n = primfacs(n)
    count_2_n = arr_n.count(2)
    count_3_n = arr_n.count(3)
    count_other_n = len(arr_n) - count_3_n - count_2_n

    arr_m = primfacs(m)
    count_2_m = arr_m.count(2)
    count_3_m = arr_m.count(3)
    count_other_m = len(arr_m) - count_3_m - count_2_m

    if count_other_m == count_other_n \
            and count_2_n <= count_2_m \
            and count_3_n <= count_3_m:
        return count_2_m + count_3_m - count_2_n - count_3_n
    else:
        return -1


print(f"{f(120, 51840)} = 7")
print(f"{f(42, 42)} = 0")
print(f"{f(48, 72)} = -1")
print(f"{f(2*2, 2)} = -1")

# n, m = list(map(int, input().split()))
# print(f(n, m))

import sys


n = int(input())

x_i = 1
z_i = n
y_i = (z_i + x_i) // 2

print(f"{x_i} {y_i} {z_i}")
sys.stdout.flush()
x_o, y_o, z_o = list(map(int, input().split()))

if x_o == 0:
    print(f"! {x_i}")
    exit(0)

s_o = 1
f_o = 0

if y_o == 0:
    s_i = x_i
    f_i = y_i
else:
    s_i = y_i
    f_i = z_i

while True:
    b_i = (s_i + f_i) // 2
    a_i = (s_i + b_i) // 2
    c_i = (b_i + f_i) // 2

    print(f"{a_i} {b_i} {c_i}")
    sys.stdout.flush()
    a_o, b_o, c_o = list(map(int, input().split()))

    if a_o == 0:
        f_i = a_i
    elif b_o == 0:
        s_i = a_i
        f_i = b_i
    elif c_o == 0:
        s_i = b_i
        f_i = c_i
    else:
        s_i = c_i

    if f_i - s_i == 1:
        print(f"! {f_i}")
        exit(0)

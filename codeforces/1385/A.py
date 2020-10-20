
def f(x, y, z):
    x_y_z = [x, y, z]
    x_y_z.sort()
    # print(x_y_z)
    if x_y_z[0] == x_y_z[1] == x_y_z[2]:
        result = x_y_z
    elif x_y_z[0] != x_y_z[1] == x_y_z[2]:
        result = [x_y_z[0], x_y_z[0], x_y_z[1]]
    elif x_y_z[0] == x_y_z[1] != x_y_z[2]:
        result = None
    elif x_y_z[0] != x_y_z[1] != x_y_z[2]:
        result = None

    return "NO" if result is None else f"YES\n{result[0]} {result[1]} {result[2]}"


if __name__ == "__main__":
    for _ in range(int(input())):
        print(f(*tuple(map(int, input().split()))))

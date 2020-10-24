
def f(n):
    c = len(str(n))
    if c == 1:
        return 10 * (n % 10 - 1) + 1
    elif c == 2:
        return 10 * (n % 10 - 1) + 3
    elif c == 3:
        return 10 * (n % 10 - 1) + 6
    else:
        return 10 * (n % 10 - 1) + 10



if __name__ == "__main__":
    for _ in range(int(input())):
        print(f(int(input())))


def f(x, y, n):
    return ((n - y) // x) * x + y


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        print(f(*tuple(map(int, input().split()))))


def f(*args, **kwargs):
    return 0


if __name__ == "__main__":
    s = input()
    n = int(input())
    m, k = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    w_arr = [int(input()) for _ in range(int(input()))]
    i_j_arr = [tuple(map(int, input().split())) for _ in range(int(input()))]
    print(f())

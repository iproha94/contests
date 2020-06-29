
def f(s):
    start_error = 0
    stack = 0
    for i, c in enumerate(s):
        stack += (1 if c == '(' else -1)
        if stack < 0:
            start_error += 1
            stack = 0

    return start_error


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        int(input())
        print(f(input()))


def f(k, arr):
    a_m_dict = {}
    for a in arr:
        m = a % k
        if m:
            a_m_dict[k - m] = a_m_dict.get(k - m, 0) + 1

    if not a_m_dict:
        return 0

    result = 0
    for key, v in a_m_dict.items():
        result = max(result, key + (v - 1) * k)

    return result + 1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = tuple(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(f(k, arr))

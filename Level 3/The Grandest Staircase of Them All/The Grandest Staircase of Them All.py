dim_n = 200
dim_k = 200
cache = [[None]*dim_k for _ in range(dim_n)]


def calculate(n, k):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if k == 0:
        return 0
    if cache[n - 1][k - 1] is None:
        cache[n - 1][k - 1] = calculate(n - k, k - 1) + calculate(n, k - 1)
    return cache[n - 1][k - 1]


def solution(n):
    return calculate(n, n - 1)

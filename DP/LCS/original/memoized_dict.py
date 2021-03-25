t = dict()


def lcs(x: str, y: str, n: int, m: int):
    if n == 0 or m == 0:
        return 0
    if (n, m) in t.keys():
        return t[(n, m)]
    if x[n - 1] == y[m - 1]:
        t[(n, m)] = 1 + lcs(x, y, n - 1, m - 1)
        return t[(n, m)]
    else:
        t[(n, m)] = max(lcs(x, y, n - 1, m), lcs(x, y, n, m - 1))
        return t[(n, m)]


X = "abcdgh"
Y = "abedfhr"

print(lcs(X, Y, len(X), len(Y)))

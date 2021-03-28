def scs(x: str, y: str, n: int, m: int):
    t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j-1])

    return m + n - t[n][m]


print(scs("geek", "eke", len("geek"), len("eke")))
print(scs("acbcf", "abcdaf", len("acbcf"), len("abcdaf")))


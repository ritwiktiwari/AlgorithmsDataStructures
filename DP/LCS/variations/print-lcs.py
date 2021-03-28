def print_lcs(x: str, y: str, m: int, n: int):
    t = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    print(t[m][n])
    i = m
    j = n
    lcs = ""
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcs = lcs + x[i - 1]
            i -= 1
            j -= 1
        else:
            if t[i - 1][j] > t[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return "".join(reversed(lcs))


a = "abcde"
b = "abfce"

print(print_lcs(a, b, len(a), len(b)))
print(print_lcs("acbcf", "abcdaf", len("acbcf"), len("abcdaf")))
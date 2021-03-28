def print_scs(x: str, y: str, n: int, m: int):
    t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    i = n
    j = m
    scs = ""

    while i > 0 and j > 0:

        if x[i - 1] == y[j - 1]:
            scs = scs + x[i - 1]
            i -= 1
            j -= 1
        else:
            if t[i - 1][j] > t[i][j - 1]:
                scs = scs + x[i - 1]
                i -= 1
            else:
                scs = scs + y[j - 1]
                j -= 1

    while i > 0:
        scs += x[i - 1]
        i -= 1
    while j > 0:
        scs += y[j - 1]
        j -= 1

    return "".join(reversed(scs))


print(print_scs("geek", "eke", len("geek"), len("eke")))
print(print_scs("acbcf", "abcdaf", len("acbcf"), len("abcdaf")))

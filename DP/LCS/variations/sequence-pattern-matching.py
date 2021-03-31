"""
Sequence pattern matching
If string A is subsequence of string B then return T else F
"""


def solve(a: str, b: str) -> bool:
    n = len(a)
    m = len(b)
    lcs = ""

    t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    i = n
    j = m

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            i -= 1
            j -= 1
            lcs += a[i]
        else:
            if t[i - 1][j] > t[i][j - 1]:
                i -= 1
            else:
                j -= 1

    lcs = "".join(reversed(lcs))

    if lcs == a:
        return True
    else:
        return False


print(solve("AXY", "ADXCPY"))

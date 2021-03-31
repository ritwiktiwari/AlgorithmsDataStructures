"""
Make a string palindrome by performing minimum deletions
(Insertions)
"""


def solve(s: str):
    n = len(s)
    s_rev = "".join(reversed(s))

    t = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s_rev[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    print(n - t[n][n])


solve("agbcba")

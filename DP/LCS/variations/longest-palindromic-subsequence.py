"""
Find Longest Palindromic Subsequence
"""


def solve(s: str):
    s_rev = "".join(reversed(s))
    n = len(s)

    t = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s_rev[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    print(t[n][n])


solve("agbcba")

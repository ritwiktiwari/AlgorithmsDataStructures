"""
Find the minimum number of insertions and deletions to convert string a to string b
"""


def solve(a: str, b: str):
    """
    Find common string (LCS)
    Deletion = len(a) - len(LCS)
    Insertion = len(b) - len(LCS)
    """
    m = len(a)
    n = len(b)

    t = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    print(f"Insertions required {len(b) - t[m][n]} Deletions required {len(a) - t[m][n]}")


solve("heap", "pea")

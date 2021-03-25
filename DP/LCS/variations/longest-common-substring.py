def longest_common_substring(x: str, y: str, n: int, m: int):
    t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    count = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
                count = max(count, t[i][j])
            else:
                t[i][j] = 0

    return count


a = "GeeksforGeeks"
b = "GeeksQuiz"

print(longest_common_substring(a, b, len(a), len(b)))

a = "abcde"
b = "abfce"

print(longest_common_substring(a, b, len(a), len(b)))
def solve(arr, d):
    n = len(arr)
    s = (sum(arr) - d) // 2

    t = [[0 for _ in range(s + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        t[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if arr[n - 1] <= s:
                t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
    return t[n][s]


my_list = [1, 1, 2, 3]
print(solve(my_list, 1))

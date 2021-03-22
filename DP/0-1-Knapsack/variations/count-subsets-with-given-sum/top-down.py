def count_subsets_with_given_sum(arr, s):
    n = len(arr)

    t = [[0 for _ in range(s + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        t[i][0] = 1
    for i in range(1, s + 1):
        t[0][i] = 0

    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
    print(t)
    return t[n][s]


my_arr = [1, 5, 11, 5]
print(count_subsets_with_given_sum(my_arr, 5))

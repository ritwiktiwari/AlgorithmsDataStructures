def subset_sum(arr, s, n):
    t = [[False for _ in range(s + 1)] for _ in range(n + 1)]

    # Initialization step
    for i in range(n + 1):
        t[i][0] = True
    for i in range(1, s + 1):
        t[0][i] = False

    # Code
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if arr[i-1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            if arr[i-1] > j:
                t[i][j] = t[i - 1][j]

    return t[n][s]


my_list = [2, 3, 7, 8, 10]
my_sum = 13
print(subset_sum(my_list, my_sum, len(my_list)))

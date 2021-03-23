def minimum_subset_sum_difference(arr):
    n = len(arr)
    s = sum(arr)

    t = [[False for _ in range(s + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        t[i][0] = True
    for i in range(s + 1):
        t[0][i] = False

    for i in range(n + 1):
        for j in range(s + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    minimized_diff = s
    for i in range(s // 2 + 1):
        if t[n][i]:
            minimized_diff = min(minimized_diff, s - (2 * i))

    return minimized_diff


my_list = [1, 6, 11, 5]
print(minimum_subset_sum_difference(my_list))
my_list = [1, 2, 7]
print(minimum_subset_sum_difference(my_list))

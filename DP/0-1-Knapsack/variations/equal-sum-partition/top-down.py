def equal_sum_partition(arr):
    n = len(arr)
    s = sum(arr) // 2

    if sum(arr) % 2 != 0:
        return False
    else:
        t = [[False for _ in range(s + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            t[i][0] = True
        for i in range(1, s + 1):
            t[0][i] = False

        for i in range(1, n + 1):
            for j in range(1, s + 1):
                if arr[i - 1] <= j:
                    t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j]
        return t[n][s]


my_arr = [1, 5, 11, 5]
print(equal_sum_partition(my_arr))

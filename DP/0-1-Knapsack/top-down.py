def knapsack(wt, val, w, n):
    for i in range(n + 1):
        for j in range(w + 1):
            if wt[i - 1] <= j:
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])
            if wt[i - 1] > j:
                t[i][j] = t[i - 1][j]
    return t[n][w]


value_list = [60, 100, 120]
weight_list = [10, 20, 30]
max_weight = 50

t = [[0 for i in range(max_weight + 1)] for j in range(len(weight_list) + 1)]

print(knapsack(weight_list, value_list, max_weight, len(weight_list)))

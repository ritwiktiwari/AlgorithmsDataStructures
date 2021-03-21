def knapsack(weight: list, value: list, w: int, n: int) -> int:
    if n == 0 or w == 0:
        return 0
    if weight[n - 1] <= w:
        return max(value[n - 1] + knapsack(weight, value, w - weight[n - 1], n - 1), knapsack(weight, value, w, n - 1))
    if weight[n - 1] > w:
        return knapsack(weight, value, w, n - 1)


value_list = [60, 100, 120]
weight_list = [10, 20, 30]
max_weight = 50

print(knapsack(weight_list, value_list, max_weight, len(weight_list)))

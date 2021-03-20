def knapsack(weight: list, value: list, w: int, n: int) -> int:
    if n == 0 or w == 0:
        return 0
    if weight[n - 1] <= w:
        return max(value[n - 1] + knapsack(weight, value, w - weight[n - 1], n - 1), knapsack(weight, value, w, n - 1))
    if weight[n - 1] > w:
        return knapsack(weight, value, w, n - 1)


weight_list = [1, 3, 4, 5]
value_list = [1, 4, 5, 7]
max_weight = 7

print(knapsack(weight_list, value_list, max_weight, len(weight_list)))
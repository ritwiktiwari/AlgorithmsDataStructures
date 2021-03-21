def knapsack(weight: list, value: list, capacity: int, n: int) -> int:
    if n == 0 or capacity == 0:
        return 0
    if t[n][capacity] != -1:
        return t[n][capacity]
    if weight[n - 1] > capacity:
        t[n][capacity] = knapsack(weight, value, capacity, n - 1)
        return t[n][capacity]
    if weight[n - 1] <= capacity:
        t[n][capacity] = max(value[n - 1] + knapsack(weight, value, capacity - weight[n - 1], n - 1),
                             knapsack(weight, value, capacity, n - 1))
        return t[n][capacity]


value_list = [60, 100, 120]
weight_list = [10, 20, 30]
max_weight = 50

t = [[-1 for i in range(max_weight + 1)] for j in range(len(weight_list) + 1)]

print(knapsack(weight_list, value_list, max_weight, len(weight_list)))

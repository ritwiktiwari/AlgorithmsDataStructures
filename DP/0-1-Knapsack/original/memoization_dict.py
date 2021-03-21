function_call_dict = dict()


def knapsack(weight: list, value: list, capacity: int, n: int) -> int:
    if n == 0 or capacity == 0:
        return 0
    if (capacity, n) in function_call_dict.keys():
        return function_call_dict[(capacity, n)]
    if weight[n - 1] > capacity:
        function_call_dict[(capacity, n)] = knapsack(weight, value, capacity, n - 1)
        return function_call_dict[(capacity, n)]
    if weight[n - 1] <= capacity:
        function_call_dict[(capacity, n)] = max(value[n - 1] + knapsack(weight, value, capacity - weight[n - 1], n - 1),
                                                knapsack(weight, value, capacity, n - 1))
        return function_call_dict[(capacity, n)]


value_list = [60, 100, 120]
weight_list = [10, 20, 30]
max_weight = 50

print(knapsack(weight_list, value_list, max_weight, len(weight_list)))

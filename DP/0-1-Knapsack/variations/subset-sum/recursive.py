def subset_sum(arr, s, n):
    if s == 0:
        return True
    if n == 0:
        return False
    if arr[n - 1] <= s:
        return subset_sum(arr, s - arr[n - 1], n - 1) or subset_sum(arr, s, n - 1)
    if arr[n - 1] > s:
        return subset_sum(arr, s, n - 1)


my_list = [2, 3, 7, 8, 10]
my_sum = 12

print(subset_sum(my_list, my_sum, len(my_list)))

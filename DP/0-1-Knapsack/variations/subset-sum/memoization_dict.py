def subset_sum(arr, s, n):
    if s == 0:
        return True
    if n == 0 and s == 0:
        return True
    if n == 0:
        return False
    if (s, n) in t.keys():
        return t[(s, n)]
    if s >= arr[n - 1]:
        t[(s, n)] = subset_sum(arr, s - arr[n - 1], n - 1) or subset_sum(arr, s, n - 1)
        return t[(s, n)]
    if s < arr[n - 1]:
        t[(s, n)] = subset_sum(arr, s, n - 1)
        return t[(s, n)]


my_list = [2, 3, 7, 8, 10]
my_sum = 11
t = dict()
print(subset_sum(my_list, my_sum, len(my_list)))

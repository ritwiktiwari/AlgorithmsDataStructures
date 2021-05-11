"""
Given a list of integers, find three integers whose product is maximum
"""
from sys import maxsize


def maximum_product_brute_force(arr):
    arr = sorted(arr)
    return max(arr[-1] * arr[-2] * arr[-3], arr[0] * arr[1] * arr[-1])


def maximum_product(arr):
    max1 = max2 = max3 = -maxsize
    min1 = min2 = maxsize
    for i in range(len(arr)):
        if arr[i] > max1:
            max3, max2, max1 = max2, max1, arr[i]
        elif arr[i] > max2:
            max3, max2 = max2, arr[i]
        elif arr[i] > max3:
            max3 = arr[i]

        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]

    return max(min1 * min2 * max1, max1 * max2 * max3)


nums = [-10, -9, 1, 2, 10]
print(maximum_product_brute_force(nums))
print(maximum_product(nums))

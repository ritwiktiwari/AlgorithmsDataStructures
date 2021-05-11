"""
Given an array move non-zeroes elements to one side of the array
"""


def mover_naive(arr):
    n = len(arr)
    new_arr = [0] * n
    index = 0
    for i in range(n):
        if arr[i] > 0:
            new_arr[index] = arr[i]
            index += 1
    return new_arr


def mover_two_pointer(arr):
    """
    Traversal pointer will traverse the array from start till the end inside the array

    Collector pointer will keep collecting the non-zero elements from the traversal pointer to thr front of the array.
    It may not be difficult to realize that all the elements between collector and traversal will be zero at the end of
    any particular iteration.

    Traversal pointer will start the traversal and will stop at non-zero element.
    Collector pointer will increment by one and then swap the values.
    """
    collector = -1
    for traversal in range(len(arr)):
        if arr[traversal] > 0:
            collector += 1
            arr[collector], arr[traversal] = arr[traversal], arr[collector]
    return arr


my_arr = [1, 0, 2, 0, 3, 0, 0, 4]
print("Naive approach:", mover_naive(my_arr))
print("Space optimized approach:", mover_two_pointer(my_arr))

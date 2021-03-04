"""
Sort an array using recursion
"""


def insert(array: list, value: int) -> list:
    """
    Insert element using recursion
    """
    if len(array) < 1 or array[-1] < value:
        array.append(value)
    else:
        temp = array.pop()
        insert(array, value)
        array.append(temp)
    return array


def insert_iterative(array: list, value: int):
    """
    Insert element iteratively
    """
    if len(array) < 1 or array[-1] < value:
        array.append(value)
    else:
        for i in range(len(array)):
            if array[i] > value:
                array.insert(i, value)
                break
    return array


def sort(array: list):
    if len(array) < 1:
        return array
    temp = array.pop()
    sort(array)
    insert(array, temp)
    return array


my_array = [5, 0, 1, 2, 9, 3]
print(sort(my_array))

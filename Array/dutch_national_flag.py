def two_colour(arr: list):
    low = 0
    high = len(arr) - 1
    while low <= high:
        if arr[low] == 0:
            low += 1
        else:
            arr[low], arr[high] = arr[high], arr[low]
            high -= 1

    print(arr)


def three_colour(arr: list):
    low = mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    print(arr)


array = [1, 0, 1, 1, 0, 0, 1, 1]
array2 = [2, 0, 1, 1, 2, 0, 1, 1]

two_colour(array)
three_colour(array2)

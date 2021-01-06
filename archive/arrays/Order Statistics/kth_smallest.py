def quicksort(arr, low, high):
    if low >= high:
        return
    else:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)


def partition(arr, low, high):
    pivot = (low+high)//2
    arr[pivot], arr[high] = arr[high], arr[pivot]
    i = low
    for j in range(low, high):
        if arr[j] <= arr[high]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def find(arr,k):
    quicksort(arr, 0, len(arr)-1)
    return arr[k-1]

# array = [23, 6, 4, -1, 0, 12, 8, 3, 1]
array = [15, 8, 5, 9, 12, 6, 7, 20]
print(find(array,2))

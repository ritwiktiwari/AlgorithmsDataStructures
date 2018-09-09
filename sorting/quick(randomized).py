import random

def quicksort(arr,low,high):
    if low>=high:
        return
    else:
        pivot = partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)

def partition(arr,low,high):
    pivot = random.randint(low,high)
    arr[pivot],arr[high] = arr[high],arr[pivot]
    i = low
    for j in range(low,high):
        if arr[j]<=arr[high]:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
    arr[i],arr[high] = arr[high],arr[i]
    return i


array = [15, 8, 5, 9, 12, 6, 7, 20]
quicksort(array, 0, len(array)-1)
print(array)


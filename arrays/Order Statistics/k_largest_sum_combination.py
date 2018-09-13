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
        if arr[j] >= arr[high]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def largest(arr1,arr2,k):
    quicksort(arr1,0,len(arr1)-1)
    quicksort(arr2,0,len(arr2)-1)
    sum_array = set()
    for i in range(k-1):
        sum_array.add(arr1[0]+arr2[i])
    for i in range(k-1):
        sum_array.add(arr1[i]+arr2[0])
    
    print(sum_array)


arr1 = [4, 2, 5, 1]
arr2 = [8, 0, 3, 5]
largest(arr1,arr2,3)

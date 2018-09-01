def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1):
        for k in range(n):
            if arr[k]>arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr


array = [15,8,6,7,20]
print(bubble_sort(array))
print(sorted(array))

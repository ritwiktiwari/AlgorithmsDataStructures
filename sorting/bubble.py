def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


array = [15, 8, 5, 9, 12,6, 7, 20]
print(bubble(array))

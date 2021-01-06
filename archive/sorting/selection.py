def selection_sort(arr):
    for i in range(0,len(arr)):
        index = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[index]:
                index = j
        if index is not i:
            arr[index],arr[i] = arr[i],arr[index]
    return arr

array = [15, 8, 6, 7, 20]
print(selection_sort(array))

def selection_sort(arr):
    for n in range(len(arr)-1,0,-1):
        print("n: ", n)
        position_of_max=0
        for k in range(1,n+1):
            if arr[k]>arr[position_of_max]:
                position_of_max=k
        arr[n], arr[position_of_max] = arr[position_of_max], arr[n]
    return arr


array = [15, 8, 6, 7, 20]
print(selection_sort(array))

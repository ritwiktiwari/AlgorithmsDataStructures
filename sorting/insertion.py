def insertion(arr):
    for i in range(1,len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr


array = [15, 8, 5, 9, 12, 6, 7, 20]
print(insertion(array))
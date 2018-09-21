def mergesort(arr,low,high):
    if low>=high :
        return
    else:
        mid = (low+high)//2
        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    tempArr = arr.copy()
    i = low
    j = mid+1
    k = low
    while i<=mid and j<=high:
        if tempArr[i]<tempArr[j]:
            arr[k]=tempArr[i]
            i+=1
        else:
            arr[k]=tempArr[j]
            j+=1
        k+=1
    while i<=mid:
        arr[k]=tempArr[i]
        i+=1
        k+=1
    while j<=high:
        arr[k]=tempArr[j]
        j+=1
        k+=1  



array = [23, 6, 4, -1, 0, 12, 8, 3, 1]
# array = [15, 8, 5, 9, 12, 6, 7, 20,-6]
mergesort(array, 0, len(array)-1)
print(array)

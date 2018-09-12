def sort(arr,low,high):
    if low>=high:
        return
    else:
        pivot = partition(arr,low,high)
        sort(arr,low,pivot-1)
        sort(arr,pivot+1,high)

def partition(arr,low,high):
    pivot = (low+high)//2
    arr[pivot],arr[high]=arr[high],arr[pivot]
    i = low
    for j in range(low,high):
        if arr[j]<=arr[high]:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[high]=arr[high],arr[i]
    return i



array = [-9,-8,-2,45,2,6,4,0,-91]
sort(array,0,len(array)-1)

print(array)
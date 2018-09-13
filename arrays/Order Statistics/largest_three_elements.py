def quicksort(arr,low,high):
    if low>=high:
        return
    else:
        pivot = partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)

def partition(arr,low,high):
    pivot = (low+high)//2
    arr[pivot],arr[high]=arr[high],arr[pivot]
    i = low
    for j in range(low,high):
        if arr[j]>=arr[high]:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[high]=arr[high],arr[i]
    return i


def largest_three(arr):
    quicksort(arr,0,len(arr)-1)
    for i in range(0,3):
        print(arr[i])


arr=[10, 4, 3, 50, 23, 90]
largest_three(arr)

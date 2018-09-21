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
        if arr[j]<=arr[high]:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[high]=arr[high],arr[i]
    return i

def mean(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    return (sum/len(arr))


def median(arr):
    n = len(arr) 
    quicksort(arr,0,n-1)
    if n%2==0:
        return ((arr[(n-1)//2] + arr[(n//2)])/2)
    else:
        return arr[n//2] 


a = [1, 3, 4, 2, 7, 5, 8, 6]
print(mean(a))
print(median(a))
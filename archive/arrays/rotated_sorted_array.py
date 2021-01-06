def binarysearch(arr,key):
    found = False
    if len(arr) == 0:
        return False
    else:
        mid = (len(arr))//2
        if arr[mid] == key:
            found = True
        else:
            if arr[mid] >= key:
                return binarysearch(arr[:mid], key)
            else:
                return binarysearch(arr[mid+1:], key)
    return found

def find(arr,key):
    pivot_index = pivot(arr)
    if key>arr[0]:
        return binarysearch(arr[:pivot_index+1], key)
    else:
        return binarysearch(arr[pivot_index+1:], key)


def pivot(arr):
    index = arr[0]
    j = 0
    while j<len(arr):
        if arr[j]>arr[index]:
            index = j
        j+=1
    return index

arr = [3,4,5,1,2]
print(find(arr,5))

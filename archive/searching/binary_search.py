def binary_ittr(arr,key):
    found = False
    first = 0
    last = len(arr)-1

    while first <= last and not found:
        mid = (first+last)//2
        if arr[mid]==key:
            found = True
        else:
            if arr[mid]>=key:
                last = mid-1
            else:
                first = mid+1
    return found


def binary_rec(arr,key):
    found = False
    if len(arr)==0:
        return False
    else:
        mid = (len(arr))//2
        if arr[mid] == key:
            found = True
        else:
            if arr[mid] >= key:
                return binary_rec(arr[:mid],key)
            else:
                return binary_rec(arr[mid+1:], key)
    return found



array = [1, 2, 4, 5, 9, 12]
print("Binary Search with iteration " , binary_ittr(array, 19))
print("Binary Search with recursion " , binary_rec(array, 19))

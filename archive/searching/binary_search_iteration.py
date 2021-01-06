def binary(arr,key):
    found = False
    left = 0
    right = len(arr)-1
    while left<=right and not found:
        mid = (left+right)//2
        if key == arr[mid]:
            found = True
            return found
        else:
            if key>arr[mid]:
                left = mid+1
            else:
                right = mid-1
    return found

array = [1, 2, 4, 5, 9, 12]
print(binary(array,88))
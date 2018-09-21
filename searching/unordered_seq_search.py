def search(arr,key):
    i = 0
    found = False
    while i < len(arr) and not found:
        if key == arr[i]:
            found = True
        else:
            i += 1
    return found


array = [2,5,4,1,9,12]
print(search(array,3))
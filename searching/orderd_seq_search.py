def search(arr,key):
    i = 0
    found = False
    stop = False

    while i < len(arr) and not found and not stop:
        if key == arr[i]:
            found = True
        else:
            if key >= arr[i]:
                i += 1
            else:
                stop = True
    return found


array = [1, 2, 4, 5, 9, 12]
print(search(array, 3))

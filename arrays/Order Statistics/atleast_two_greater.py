def atleast_two_greater(arr):
    first = arr[0]
    second = arr[0]
    for i in range(len(arr)):
        if arr[i]>first:
            second = first
            first = arr[i]
        elif arr[i]>second:
            second = arr[i]
    print("First Largest = ",first)
    print("Second Largest = ",second)
    for i in range(len(arr)):
        if arr[i]<second:
            print(arr[i])


array = [2, 8, 7, 1, 5]
atleast_two_greater(array)

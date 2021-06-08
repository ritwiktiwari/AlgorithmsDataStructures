def minJumps(arr, n):
    count = 0
    i = 0
    while i < n-1:

        count += 1
        i = i + arr[i]
        # print(i)

    print(count)


array = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
array2 = [1, 1, 2, 4, 7, 3, 5, 2, 1]
array3 = [1, 4, 3, 2, 6, 7]
print(minJumps(array, 11))
print(minJumps(array2, 9))
print(minJumps(array3, 6))

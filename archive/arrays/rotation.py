def rotate(arr,r):
    i=0
    while i<r:
        temp = arr[0]
        for j in range(len(arr)-1):
            arr[j]=arr[j+1]
        arr[-1]=temp
        i+=1
    return arr

arr = [1,2,3,4,5]
print(rotate(arr,2))
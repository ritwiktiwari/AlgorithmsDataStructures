def move(arr,low,high):
    if low>=high:
        return
    else:
        index = moveZeroes(arr,low,high)
        move(arr,low,index-1)
        move(arr,index+1,high)

def moveZeroes(arr,low,high):
    pivot = (low+high)//2
    arr[pivot],arr[high]=arr[high],arr[pivot]
    i = low
    for j in range(low,high):
        if arr[j]==0:
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
    arr[i],arr[high]=arr[high],arr[i]
    return i

array = [1,2,0,3,4,0,5,0,41,0]
move(array,0,len(array)-1)
print(array)

    
    
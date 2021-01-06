# Approach (1)
# def move(arr,low,high):
#     if low>=high:
#         return
#     else:
#         index = moveZeroes(arr,low,high)
#         move(arr,low,index-1)
#         move(arr,index+1,high)

# def moveZeroes(arr,low,high):
#     pivot = (low+high)//2
#     arr[pivot],arr[high]=arr[high],arr[pivot]
#     i = low
#     for j in range(low,high):
#         if arr[j]==0:
#             arr[j],arr[i]=arr[i],arr[j]
#             i+=1
#     arr[i],arr[high]=arr[high],arr[i]
#     return i

# Appraoch (2)

# def move(arr):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] is not 0:
#             arr[count]=arr[i]
#             count +=1
#     while count<len(arr):
#         arr[count]=0
#         count+=1

# Approach 3
def move(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] is not 0:
            arr[count],arr[i]=arr[i],arr[count]
            count+=1
array = [1,2,0,3,4,0,5,0,41,0]
# move(array,0,len(array)-1)  #Approach 1
move(array) # Approach 2 and 3
print(array)

    
    
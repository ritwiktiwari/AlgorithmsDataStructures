import random
def combination(arr1,arr2,k):
    i=0
    while i <k:
        rand1 = random.randint(0,len(arr1)-1)
        rand2 = random.randint(0,len(arr2)-1)
        print(arr1[rand1]+arr2[rand2])
        i+=1

arr1 = [3,2]
arr2 = [1,4]
combination(arr1,arr2,2)

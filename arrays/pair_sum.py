def pair_sum(arr, k):
    counter = 0
    lookup = set()
    for num in arr:
        print("num ",num)
        print("lookup ",lookup)
        print("counter ",counter)
        if k-num in lookup:
            counter += 1
        else:
            lookup.add(num)
    return counter


pair_sum([1, 3, 2, 2], 4)

def find_missing_number(arr: list):
    ans = len(arr) + 1
    # ans = 0
    for i in range(len(arr)):
        ans = ans ^ arr[i]
        ans = ans ^ (i + 1)

        print(arr[i], ans ^ i, ans ^ arr[i])

    print(ans)


nums = [1, 3, 2, 5]
find_missing_number(nums)

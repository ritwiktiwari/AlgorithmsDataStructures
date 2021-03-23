def findTargetSumWays(nums, S: int) -> int:
    s = sum(nums)
    if S > s:
        return 0
    if (s + S) % 2 != 0:
        return 0

    n = len(nums)
    s = (s - S) // 2

    t = [[0 for _ in range(s + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        t[i][0] = 1
    # for i in range(1, s + 1):
    # t[0][i] = 0

    for i in range(1, n + 1):
        for j in range(s + 1):
            if nums[i - 1] <= j:
                t[i][j] = t[i - 1][j - nums[i - 1]] + t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
    return t[n][s]

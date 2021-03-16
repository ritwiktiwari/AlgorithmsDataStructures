"""
k-th symbol in grammar
"""


def invert(x: int) -> int:
    if x == 1:
        return 0
    else:
        return 1


def k_symbol(n: int, k: int) -> int:
    mid = 2 ** (n - 2)
    if k == 1 and n == 1:
        return 0
    if k <= mid:
        return k_symbol(n - 1, k)
    elif k > mid:
        return invert(k_symbol(n - 1, k - mid))


print(k_symbol(4, 2))

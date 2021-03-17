"""
Josephus Problem
Execution in circle
"""


def execution_in_circle(n: int, k: int):
    k = k - 1

    def inner(arr: list, pos: int):
        if len(arr) == 1:
            return arr
        else:
            pos = (pos + k) % len(arr)
            arr.pop(pos)
            return inner(arr, pos)

    return inner(list(range(1, n + 1)), 0)


print(execution_in_circle(12, 3))

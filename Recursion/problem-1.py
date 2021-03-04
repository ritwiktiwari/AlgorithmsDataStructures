"""
Print 1 to n using recursion
"""


def recursive_print(n: int):
    if n < 1:
        return
    recursive_print(n - 1)
    print(n)


recursive_print(10)

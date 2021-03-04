"""
Print n to 1 using recursion
"""


def recursive_print(n: int):
    if n < 1:
        return
    print(n)
    recursive_print(n - 1)


recursive_print(10)

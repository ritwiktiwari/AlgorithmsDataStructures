"""
Find sum of positive number using recursion
"""


def sum_of_digits(n: int):
    assert 0 <= n == int(n), "The number has to be a positive integer only!"
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)


s = sum_of_digits(1234)
print(s)
print(sum_of_digits(-9))

"""
Calculate power of number using recursion
"""


def power(base: int, exp: int):
    assert base == int(base), "x must be an integer"
    assert 0 <= exp == int(exp), "y must be >= 0"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp - 1)


print(power(5, 3))
print(power(-2, 3))
print(power(-2, 2))

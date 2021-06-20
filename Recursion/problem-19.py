"""
Find greatest common divisor using recursion
"""


def gcd(a: int, b: int):
    assert a == int(a) and b == int(b), "a and b must be integers"
    if a != 0 and b == 0:
        return a
    # if a % b == 0:
    #     return b
    return gcd(b, a % b)


print(gcd(48, 18))
print(gcd(48, 0))

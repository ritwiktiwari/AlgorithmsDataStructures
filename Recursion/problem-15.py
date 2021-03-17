"""
Print n-bit binary prefix where #1 >= #0
"""


def n_bit_binary(n: int, one: int, zero: int, string: str):
    if n == 0:
        print(string)
        return
    output1 = string + '1'
    n_bit_binary(n - 1, one + 1, zero, output1)
    if one > zero:
        output2 = string + '0'
        n_bit_binary(n - 1, one, zero + 1, output2)


n_bit_binary(3, 0, 0, "")

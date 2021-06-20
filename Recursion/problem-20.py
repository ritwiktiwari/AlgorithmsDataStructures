"""
Convert decimal to binary
"""


def convert(x: int):
    if x == 0:
        print()
        return
    convert(x // 2)
    print(x % 2, end="")


convert(13)
convert(10)

"""
Generate balanced parenthesis
"""


def generate_balanced_parenthesis(n: int):
    def inner(opening: int, closing: int, string: str):
        if opening == 0 and closing == 0:
            print(string)
            return
        if opening != 0:
            output1 = string + "("
            inner(opening - 1, closing, output1)
        if closing > opening:
            output2 = string + ")"
            inner(opening, closing - 1, output2)

    inner(n, n, "")


generate_balanced_parenthesis(3)

"""
Generate all balanced parenthesis
"""


def generate_balanced_parenthesis_helper(opening: int, closing: int, string: str):
    if opening == 0 and closing == 0:
        print(string)
        return
    if opening != 0:
        output1 = string + "("
        generate_balanced_parenthesis_helper(opening - 1, closing, output1)
    if opening < closing:
        output2 = string + ")"
        generate_balanced_parenthesis_helper(opening, closing - 1, output2)


def generate_balanced_parenthesis(n: int):
    generate_balanced_parenthesis_helper(n, n, "")


generate_balanced_parenthesis(2)

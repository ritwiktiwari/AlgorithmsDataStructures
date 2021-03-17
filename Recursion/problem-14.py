"""
Generate balanced parenthesis
"""


def generate_balanced_parenthesis(opening: int, closing: int, string: str):
    if opening == 0 and closing == 0:
        print(string)
    if opening != 0:
        output1 = string + "("
        generate_balanced_parenthesis(opening - 1, closing, output1)
    if closing > opening:
        output2 = string + ")"
        generate_balanced_parenthesis(opening, closing - 1, output2)


generate_balanced_parenthesis(3, 3, "")

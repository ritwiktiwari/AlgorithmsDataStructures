"""
Permutation with spaces
"""


def permutation_with_spaces(input_string: str, output: str):
    if len(input_string) < 1:
        print(output, end="\n")
        return
    else:
        output1 = output + " " + input_string[0]
        output2 = output + input_string[0]
        input_string = input_string[1:]
        permutation_with_spaces(input_string, output1)
        permutation_with_spaces(input_string, output2)


my_string = "ABC"
permutation_with_spaces(my_string[1:], my_string[0])

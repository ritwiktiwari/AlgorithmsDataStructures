"""
Letter case permutation
"""


def lettercase_permutation(input_string: str, output_string: str):
    if len(input_string) < 1:
        print(output_string)
        return
    elif input_string[0].isalpha():
        output1 = output_string + input_string[0].upper()
        output2 = output_string + input_string[0].lower()
        input_string = input_string[1:]
        lettercase_permutation(input_string, output1)
        lettercase_permutation(input_string, output2)
    else:
        output1 = output_string + input_string[0].upper()
        input_string = input_string[1:]
        lettercase_permutation(input_string, output1)


lettercase_permutation("a1b2", "")

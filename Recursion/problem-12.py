"""
Permutation with case change
"""


def permutation_with_case_change(input_string: str, output_string: str):
    if len(input_string) < 1:
        print(output_string)
        return
    else:

        output_string1 = output_string + input_string[0].upper()
        output_string2 = output_string + input_string[0]
        input_string = input_string[1:]
        permutation_with_case_change(input_string, output_string1)
        permutation_with_case_change(input_string, output_string2)


permutation_with_case_change("ab", "")

"""
Printing all subsequences
"""


def subsequence(input_string: str, output_string: str):
    if len(input_string) < 1:
        print(output_string, end='\n')
        return
    else:
        output1 = output_string
        output2 = output_string + input_string[0]
        input_string = input_string[1:]
        subsequence(input_string, output1)
        subsequence(input_string, output2)


unique_subsequence_set = set()


def unique_subsequence(input_string: str, output_string: str):
    global unique_subsequence_set
    if len(input_string) < 1:
        unique_subsequence_set.add(output_string)
        return
    else:
        output1 = output_string
        output2 = output_string + input_string[0]
        input_string = input_string[1:]
        unique_subsequence(input_string, output1)
        unique_subsequence(input_string, output2)


# subsequence("abc", "")
unique_subsequence("aac", "")
print(unique_subsequence_set)
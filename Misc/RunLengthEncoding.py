def run_length_encoding(string: str):
    consecutive_char_count = 1
    encoded_string = ""
    for i in range(1, len(string)):
        if string[i - 1] != string[i]:
            encoded_string = encoded_string + str(consecutive_char_count) + string[i - 1]
            consecutive_char_count = 1
        else:
            consecutive_char_count += 1
    encoded_string = encoded_string + str(consecutive_char_count) + string[-1]
    return encoded_string


print(run_length_encoding("aaaabbcccfff"))

def longest_common_prefix(strings: list):
    for col in range(len(strings[0])):
        prefix = strings[0][col]
        for row in range(1, len(strings)):
            if (col >= len(strings[row])) or (prefix != strings[row][col]):
                return strings[0][:col]
    return strings[0]


print(longest_common_prefix(["flower", "flow", "flowInsight"]))
print(longest_common_prefix(["cat", "caterpillar", "catylic"]))
print(longest_common_prefix(["ram", "sham", "ramesh"]))

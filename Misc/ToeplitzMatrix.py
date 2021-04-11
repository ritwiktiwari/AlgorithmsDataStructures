def is_toeplitz(matrix: list) -> bool:
    for row in range(len(matrix) - 1):
        for col in range(len(matrix[row]) - 1):
            if matrix[row][col] != matrix[row + 1][col + 1]:
                return False
    return True


print(is_toeplitz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(is_toeplitz([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))

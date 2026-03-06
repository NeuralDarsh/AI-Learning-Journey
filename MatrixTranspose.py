# Bridging Linear Algebra with Python Programming

def transpose_matrix(matrix):
    # Using nested list comprehension to flip the matrix
    # Rows become columns and columns become rows
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result

if __name__ == "__main__":
    # A 3x2 Matrix (3 rows, 2 columns)
    my_matrix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    print("--- Linear Algebra: Matrix Transposer ---")
    print("Original Matrix:")
    for row in my_matrix:
        print(row)

    transposed = transpose_matrix(my_matrix)

    print("\nTransposed Matrix (2x3):")
    for row in transposed:
        print(row)
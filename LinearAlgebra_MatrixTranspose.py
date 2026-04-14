# Practicing Matrix Operations for 4th Semester coursework and AI

import numpy as np

def matrix_operations():
    # 1. Define a 3x2 Matrix (3 rows, 2 columns)
    # This could represent 3 students and their marks in 2 subjects
    matrix = np.array([[85, 90], 
                       [78, 88], 
                       [92, 95]])

    print("--- Linear Algebra: Matrix Transpose ---")
    print(f"Original Matrix (Shape {matrix.shape}):\n{matrix}")

    # 2. Perform Transpose (Switch Rows and Columns)
    # Using the .T attribute in NumPy
    transposed = matrix.T

    print(f"\nTransposed Matrix (Shape {transposed.shape}):\n{transposed}")

    # 3. Check for Symmetry (Property check)
    # A matrix is symmetric if Matrix == Matrix.T
    # We'll use a Square Matrix for this example
    square_matrix = np.array([[1, 2], 
                              [2, 1]])
    
    is_symmetric = np.array_equal(square_matrix, square_matrix.T)
    
    print("\n---  Property Check ---")
    print(f"Is the square matrix symmetric? {is_symmetric}")

if __name__ == "__main__":
    matrix_operations()
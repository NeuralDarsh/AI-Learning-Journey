# Applying Linear Algebra concepts for Machine Learning

import numpy as np

def matrix_op():
    # 1. Define a 2x3 Matrix (e.g., Input Data)
    # 2 rows, 3 columns
    A = np.array([[1, 2, 3], 
                  [4, 5, 6]])

    # 2. Define a 3x2 Matrix (e.g., Weights in a Neural Network)
    # 3 rows, 2 columns (Columns of A must match Rows of B!)
    B = np.array([[7, 8], 
                  [9, 10], 
                  [11, 12]])

    print("---  Linear Algebra: Matrix Multiplication ---")
    print(f"Matrix A (Shape {A.shape}):\n{A}")
    print(f"\nMatrix B (Shape {B.shape}):\n{B}")

    # 3. Perform Dot Product (Matrix Multiplication)
    # We use np.dot() or the @ operator
    result = np.dot(A, B)

    print(f"\nResulting Matrix (Shape {result.shape}):")
    print(result)

    #  Logic Check for your exam:
    # (2x3) * (3x2) results in a (2x2) matrix.
    print(f"\nNote: The inner dimensions (3) matched, so the output is {result.shape}.")

if __name__ == "__main__":
    matrix_op()
# Bridging Linear Algebra theory with NumPy verification logic

import numpy as np

def check_orthogonality():
    print("---  直交行列チェッカー (Orthogonal Matrix Checker) ---")
    
    # 1. Define an orthogonal matrix (Standard Rotation Matrix for 90 degrees)
    # Cos(90)=0, Sin(90)=1. 
    matrix = np.array([[0, -1], 
                       [1,  0]])

    print(f"Original Matrix (A):\n{matrix}\n")

    # 2. Get the Transpose (A^T)
    matrix_transpose = matrix.T
    print(f"Transposed Matrix (A^T):\n{matrix_transpose}\n")

    # 3. Multiply A by A^T
    product = np.dot(matrix, matrix_transpose)
    
    # 4. Check if the product equals the Identity Matrix (I)
    identity_matrix = np.eye(matrix.shape[0])
    
    # Using np.allclose to handle tiny floating-point precision differences
    if np.allclose(product, identity_matrix):
        print(" Result: The matrix is ORTHOGONAL! (A * A^T = I)")
    else:
        print(" Result: The matrix is NOT orthogonal.")

if __name__ == "__main__":
    check_orthogonality()
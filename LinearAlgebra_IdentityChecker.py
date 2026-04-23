# Practicing Matrix validation and NumPy identity functions

import numpy as np

def check_matrix_properties():
    print("---  Linear Algebra: Identity Matrix Checker ---")
    
    # 1. Create a 3x3 Identity Matrix automatically
    identity_3x3 = np.eye(3)
    print(f"Standard 3x3 Identity Matrix (I):\n{identity_3x3}\n")

    # 2. User Input Simulation
    # Let's define a test matrix
    test_matrix = np.array([[1, 0, 0], 
                            [0, 1, 0], 
                            [0, 0, 1]])

    # 3. Check if it is an Identity Matrix
    # np.array_equal checks if shapes and elements are identical
    if np.array_equal(test_matrix, np.eye(test_matrix.shape[0])):
        print(" Result: This is a valid Identity Matrix!")
    else:
        print(" Result: This is NOT an Identity Matrix.")

    # 4. Bonus: Check if it's a Scalar Matrix (Diagonal elements are equal)
    diag = np.diag(test_matrix)
    if np.all(diag == diag[0]) and np.array_equal(test_matrix, np.diag(diag)):
        print(f" Note: This is also a Scalar Matrix with value {diag[0]}.")

if __name__ == "__main__":
    check_matrix_properties()
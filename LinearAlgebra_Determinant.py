# Practicing NumPy Linear Algebra (linalg) module for 4th Sem studies

import numpy as np

def calculate_determinant():
    print("---  Linear Algebra: Determinant Calculator ---")
    
    # 1. Define a 2x2 or 3x3 Square Matrix
    # (Determinants only exist for square matrices)
    matrix = np.array([[4, 7], 
                       [2, 6]])

    print(f"Matrix:\n{matrix}")

    # 2. Use NumPy's linalg.det() function
    det = np.linalg.det(matrix)
    
    # 3. Rounding because float operations can have tiny errors
    det = round(det, 2)

    print(f"\nDeterminant: {det}")

    # 4. Property Logic: Singularity
    # If Det = 0, the matrix is "Singular" (cannot be inverted)
    if det == 0:
        print(" This is a Singular Matrix (No Inverse exists).")
    else:
        print(" This is a Non-Singular Matrix (Inverse exists).")

if __name__ == "__main__":
    calculate_determinant()
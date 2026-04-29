# Bridging Linear Algebra theory with NumPy's linalg module

import numpy as np

def analyze_matrix_rank():
    print("---  Linear Algebra: Matrix Rank Analyzer ---")
    
    # 1. Define a Matrix
    # Example: Row 3 is just Row 1 + Row 2 (Redundant information)
    matrix = np.array([[1, 2, 3], 
                       [4, 5, 6], 
                       [5, 7, 9]])

    print(f"Matrix:\n{matrix}")

    # 2. Calculate Rank using NumPy
    rank = np.linalg.matrix_rank(matrix)
    
    # 3. Determine if it's "Full Rank"
    rows, cols = matrix.shape
    is_full_rank = rank == min(rows, cols)

    print(f"\nMatrix Rank: {rank}")
    print(f"Matrix Dimensions: {rows}x{cols}")

    if is_full_rank:
        print(" This is a Full Rank matrix (All rows/cols are linearly independent).")
    else:
        print(" This matrix is Rank Deficient (Contains redundant/dependent rows).")

if __name__ == "__main__":
    analyze_matrix_rank()
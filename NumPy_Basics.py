# The foundation for all AI and Machine Learning calculations

import numpy as np

def explore_numpy():
    # 1. Creating a NumPy Array (Faster than a Python List)
    my_list = [1, 2, 3, 4, 5]
    np_array = np.array(my_list)
    
    print("---  NumPy vs Python Lists ---")
    print(f"Standard List: {my_list}")
    print(f"NumPy Array:   {np_array}")

    # 2. Vectorized Operations (Math on the whole array at once!)
    # In regular Python, you'd need a loop. In NumPy, just one line:
    doubled_array = np_array * 2
    squared_array = np_array ** 2

    print(f"\nDoubled: {doubled_array}")
    print(f"Squared: {squared_array}")

    # 3. Multi-dimensional Arrays (Matrices for Linear Algebra)
    matrix = np.array([[1, 2], [3, 4]])
    print("\n2x2 Matrix (Linear Algebra Concept):")
    print(matrix)
    print(f"Shape of Matrix: {matrix.shape}")

if __name__ == "__main__":
    explore_numpy()
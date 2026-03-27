# Practical Application for 4th Semester Linear Algebra

import numpy as np

def solve_equations():
    print("---  Linear Algebra: Equation Solver ---")
    print("Solving for x and y in:")
    print("3x + y = 9")
    print("x + 2y = 8\n")

    # 1. Create the Coefficient Matrix (A)
    # [3, 1] from (3x + 1y)
    # [1, 2] from (1x + 2y)
    A = np.array([[3, 1], [1, 2]])

    # 2. Create the Constants Matrix (B)
    B = np.array([9, 8])

    # 3. Solve for X (Inverse of A multiplied by B)
    # linalg.solve handles the heavy matrix math for you
    solution = np.linalg.solve(A, B)

    x = solution[0]
    y = solution[1]

    print(f"Results:")
    print(f"Value of x: {x:.2f}")
    print(f"Value of y: {y:.2f}")

    # Verification: 3(2) + 3 = 9? Yes!
    print(f"\nVerification: 3({x}) + {y} = {3*x + y}")

if __name__ == "__main__":
    solve_equations()